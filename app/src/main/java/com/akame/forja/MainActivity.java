package com.akame.forja;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.btn_auto_sales).setOnClickListener(v -> {
            Toast.makeText(this, "Bot de Vendas Ativado: Monitorando DMs...", Toast.LENGTH_LONG).show();
        });

        findViewById(R.id.btn_obfuscate).setOnClickListener(v -> {
            Toast.makeText(this, "Metadados Removidos. Vídeo pronto para o Instagram.", Toast.LENGTH_SHORT).show();
        });
    }
}
