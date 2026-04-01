package com.imperio.app;
import android.app.Activity;
import android.content.*;
import android.os.*;
import android.view.*;
import android.widget.*;
import android.graphics.Color;

public class MainActivity extends Activity {
    private LinearLayout mainLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setupLoginView();
    }

    private void setupLoginView() {
        setContentView(R.layout.activity_main);
        final EditText pin = findViewById(R.id.pinInput);
        findViewById(R.id.btnEntrar).setOnClickListener(v -> {
            if (pin.getText().toString().equals("3650") || pin.getText().toString().equalsIgnoreCase("Milton")) {
                openNexusDashboard();
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void openNexusDashboard() {
        mainLayout = new LinearLayout(this);
        mainLayout.setOrientation(LinearLayout.VERTICAL);
        mainLayout.setBackgroundColor(Color.BLACK);
        mainLayout.setPadding(30, 50, 30, 30);

        addHeader("NEXUS DASHBOARD");
        
        // Módulo 1: Monitor de Sistema
        TextView stats = new TextView(this);
        stats.setText("SISTEMA: ESTÁVEL\nBATERIA: 100%\nMEMÓRIA: OTIMIZADA");
        stats.setTextColor(Color.GREEN);
        stats.setPadding(0, 20, 0, 40);
        mainLayout.addView(stats);

        // Módulo 2: Terminal Remoto (Interface)
        addHeader("TERMINAL COMANDOS");
        EditText cmdInput = new EditText(this);
        cmdInput.setHint("Digite comando Termux...");
        cmdInput.setHintTextColor(Color.GRAY);
        cmdInput.setTextColor(Color.WHITE);
        mainLayout.addView(cmdInput);

        Button btnExec = new Button(this);
        btnExec.setText("EXECUTAR NO TERMUX");
        btnExec.setBackgroundColor(0xFFFFD700);
        btnExec.setOnClickListener(v -> Toast.makeText(this, "Comando enviado ao Termux!", Toast.LENGTH_SHORT).show());
        mainLayout.addView(btnExec);

        // Módulo 3: Cofre de Segredos
        addHeader("COFRE DE SEGREDOS");
        Button btnVault = new Button(this);
        btnVault.setText("ABRIR ARQUIVOS CRIPTOGRAFADOS");
        btnVault.setOnClickListener(v -> Toast.makeText(this, "Acessando banco de dados seguro...", Toast.LENGTH_LONG).show());
        mainLayout.addView(btnVault);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(mainLayout);
        setContentView(scroll);
    }

    private void addHeader(String text) {
        TextView header = new TextView(this);
        header.setText(text);
        header.setTextColor(0xFFFFD700);
        header.setTextSize(18);
        header.setPadding(0, 30, 0, 10);
        mainLayout.addView(header);
    }
}
