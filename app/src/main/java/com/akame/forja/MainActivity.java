package com.akame.forja;

import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private ProgressBar progressSync;
    private FrameLayout callOverlay;
    private VideoView videoView;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        progressSync = findViewById(R.id.progress_sync);
        callOverlay = findViewById(R.id.call_overlay);
        videoView = findViewById(R.id.video_view);
        listView = findViewById(R.id.listView);

        // BOTÃO DE SINCRONIZAÇÃO
        findViewById(R.id.btn_sync_cloud).setOnClickListener(v -> {
            executarSincronizacao();
        });

        findViewById(R.id.btn_fake_call).setOnClickListener(v -> {
            callOverlay.setVisibility(View.VISIBLE);
            String path = "android.resource://" + getPackageName() + "/" + R.raw.video_influencer;
            videoView.setVideoURI(Uri.parse(path));
            videoView.start();
        });

        findViewById(R.id.btn_end_call).setOnClickListener(v -> {
            callOverlay.setVisibility(View.GONE);
            videoView.stopPlayback();
        });

        atualizarLista();
    }

    private void executarSincronizacao() {
        progressSync.setVisibility(View.VISIBLE);
        dbHelper.addData("🔄 INICIANDO PUSH PARA GITHUB...");
        atualizarLista();

        // Simula o tempo de upload para o GitHub
        new Handler().postDelayed(() -> {
            progressSync.setVisibility(View.GONE);
            dbHelper.addData("✅ NUVEM ATUALIZADA: Versão 1.0.4 enviada.");
            atualizarLista();
            Toast.makeText(this, "Sincronização com GitHub Concluída!", Toast.LENGTH_LONG).show();
        }, 3000);
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
