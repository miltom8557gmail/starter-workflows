package com.nexus.app;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        Button btnSocial = findViewById(R.id.btn_social);
        Button btnAuto = findViewById(R.id.btn_auto);
        TextView log = findViewById(R.id.log_status);

        btnSocial.setOnClickListener(v -> {
            log.setText("SISTEMA: SINCRONIZANDO NODES...");
            Toast.makeText(this, "Acessando APIs Externas", Toast.LENGTH_SHORT).show();
        });

        btnAuto.setOnClickListener(v -> {
            log.setText("SISTEMA: BOT EM EXECUÇÃO MÁXIMA 🛡️");
            btnAuto.setText("BOT ATIVO");
            btnAuto.setEnabled(false);
            Toast.makeText(this, "Automação Soberana v5.0 Iniciada!", Toast.LENGTH_LONG).show();
        });
    }
}
