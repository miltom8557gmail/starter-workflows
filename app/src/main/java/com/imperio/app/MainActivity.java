package com.imperio.app;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.*;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        showLogin();
    }

    private void showLogin() {
        setContentView(R.layout.activity_main);
        final EditText pinInput = findViewById(R.id.pinInput);
        Button btnEntrar = findViewById(R.id.btnEntrar);
        btnEntrar.setOnClickListener(v -> {
            String pin = pinInput.getText().toString();
            if (pin.equals("3650") || pin.equalsIgnoreCase("Milton")) {
                showDashboard();
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void showDashboard() {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setGravity(17);
        layout.setBackgroundColor(0xFF000000);

        TextView tv = new TextView(this);
        tv.setText("PAINEL DE CONTROLE NEXUS\nBEM-VINDO, MESTRE");
        tv.setTextColor(0xFFFFD700);
        tv.setTextSize(24);
        tv.setGravity(17);

        Button btnStatus = new Button(this);
        btnStatus.setText("VERIFICAR SISTEMA");
        btnStatus.setBackgroundColor(0xFFFFD700);
        btnStatus.setOnClickListener(v -> Toast.makeText(this, "TODOS OS MÓDULOS OPERACIONAIS", Toast.LENGTH_LONG).show());

        layout.addView(tv);
        layout.addView(btnStatus);
        setContentView(layout);
    }
}
