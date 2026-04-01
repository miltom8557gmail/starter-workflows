package com.imperio.app;
import android.app.Activity;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.*;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText pinInput = findViewById(R.id.pinInput);
        Button btnEntrar = findViewById(R.id.btnEntrar);
        btnEntrar.setOnClickListener(v -> {
            if (pinInput.getText().toString().equals("3650") || pinInput.getText().toString().equalsIgnoreCase("Milton")) {
                showDashboard();
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });
    }
    private void showDashboard() {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setGravity(Gravity.CENTER);
        layout.setBackgroundColor(0xFF000000);
        TextView tv = new TextView(this);
        tv.setText("NEXUS DASHBOARD\nSISTEMA OPERACIONAL");
        tv.setTextColor(0xFFFFD700);
        tv.setTextSize(22);
        tv.setGravity(Gravity.CENTER);
        layout.addView(tv);
        setContentView(layout);
    }
}
