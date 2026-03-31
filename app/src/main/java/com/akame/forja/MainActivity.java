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
            startFakeCall();
        });

        findViewById(R.id.btn_end_call).setOnClickListener(v -> {
            callOverlay.setVisibility(View.GONE);
            videoView.stopPlayback();
            dbHelper.addData("CHAMADA ENCERRADA: Sucesso na prova social.");
            atualizarLista();
        });

        findViewById(R.id.btn_obfuscate).setOnClickListener(v -> {
            dbHelper.addData("MÍDIA PROTEGIDA: Metadados Exif removidos.");
            atualizarLista();
            Toast.makeText(this, "🛡️ Proteção Anti-Ban Aplicada!", Toast.LENGTH_SHORT).show();
        });

        atualizarLista();
    }

    private void startFakeCall() {
        callOverlay.setVisibility(View.VISIBLE);
        // O vídeo deve estar na pasta res/raw/video_influencer.mp4
        String path = "android.resource://" + getPackageName() + "/" + R.raw.video_influencer;
        videoView.setVideoURI(Uri.parse(path));
        videoView.start();
        dbHelper.addData("LIVE INICIADA: Simulando presença...");
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
