package com.akame.nexus;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        // Permissões de Elite
        String[] permissions = {
            Manifest.permission.RECORD_AUDIO,
            Manifest.permission.CAMERA,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
        };

        if (ActivityCompat.checkSelfPermission(this, permissions[0]) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, permissions, 100);
        }

        Button btnArsenal = findViewById(R.id.btnArsenal);
        Button btnBunker = findViewById(R.id.btnBunker);

        // Ativação da Ponte de Dados
        btnBunker.setOnClickListener(v -> {
            Intent serviceIntent = new Intent(MainActivity.this, AkameService.class);
            startService(serviceIntent);
            Toast.makeText(MainActivity.this, "📡 Bunker Sincronizado!", Toast.LENGTH_SHORT).show();
        });

        // O Gatilho do Arsenal (Passo 4)
        btnArsenal.setOnClickListener(v -> {
            // Aqui enviamos o comando para o serviço processar
            Intent intent = new Intent("AKAME_COMMAND");
            intent.putExtra("cmd", "open_arsenal");
            sendBroadcast(intent);
            Toast.makeText(MainActivity.this, "⚔️ Despertando Arsenal no Termux...", Toast.LENGTH_SHORT).show();
        });
    }
}
