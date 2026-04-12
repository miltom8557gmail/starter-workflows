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

        btnBunker.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent serviceIntent = new Intent(MainActivity.this, AkameService.class);
                startService(serviceIntent);
                Toast.makeText(MainActivity.this, "📡 Ponte Akame Ativada!", Toast.LENGTH_LONG).show();
            }
        });

        btnArsenal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "⚔️ Arsenal aguardando Passo 4...", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
