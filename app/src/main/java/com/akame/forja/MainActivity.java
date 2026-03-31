package com.akame.forja;

import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private FrameLayout callOverlay;
    private VideoView videoView;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        callOverlay = findViewById(R.id.call_overlay);
        videoView = findViewById(R.id.video_view);
        listView = findViewById(R.id.listView);

        findViewById(R.id.btn_fake_call).setOnClickListener(v -> {
            try {
                callOverlay.setVisibility(View.VISIBLE);
                // Busca o vídeo na pasta raw
                String path = "android.resource://" + getPackageName() + "/" + R.raw.video_influencer;
                videoView.setVideoURI(Uri.parse(path));
                videoView.start();
                dbHelper.addData("LIVE: Chamada iniciada para verificação.");
            } catch (Exception e) {
                Toast.makeText(this, "Erro: Adicione o vídeo na pasta res/raw", Toast.LENGTH_LONG).show();
                callOverlay.setVisibility(View.GONE);
            }
        });

        findViewById(R.id.btn_end_call).setOnClickListener(v -> {
            callOverlay.setVisibility(View.GONE);
            videoView.stopPlayback();
            dbHelper.addData("LIVE: Chamada encerrada com sucesso.");
            atualizarLista();
        });

        findViewById(R.id.btn_obfuscate).setOnClickListener(v -> {
            dbHelper.addData("SECURITY: Metadados eliminados.");
            atualizarLista();
            Toast.makeText(this, "🛡️ Camuflagem Aplicada!", Toast.LENGTH_SHORT).show();
        });

        atualizarLista();
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
