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
        
        Button btnAuto = findViewById(R.id.btn_auto);
        TextView log = findViewById(R.id.log_status);

        btnAuto.setOnClickListener(v -> {
            log.setText("🚀 MÓDULOS DE IA & DEEPFAKE: ONLINE");
            Toast.makeText(this, "Nexus v5.1: Soberania Ativada", Toast.LENGTH_LONG).show();
        });
    }
}
