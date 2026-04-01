package com.imperio.app;
import android.app.Activity;
import android.os.*;
import android.view.Gravity;
import android.widget.*;
import android.graphics.Color;
import android.content.Intent;
import android.content.IntentFilter;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText pin = findViewById(R.id.pinInput);
        findViewById(R.id.btnEntrar).setOnClickListener(v -> {
            if (pin.getText().toString().equals("3650") || pin.getText().toString().equalsIgnoreCase("Milton")) {
                openDashboard();
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });
    }
    private void openDashboard() {
        LinearLayout ly = new LinearLayout(this);
        ly.setOrientation(LinearLayout.VERTICAL);
        ly.setBackgroundColor(Color.BLACK);
        ly.setPadding(40, 60, 40, 40);
        ly.setGravity(Gravity.CENTER);
        
        TextView t = new TextView(this);
        t.setText("SISTEMA NEXUS ONLINE\nBEM-VINDO, MESTRE");
        t.setTextColor(0xFFFFD700);
        t.setTextSize(24);
        t.setGravity(Gravity.CENTER);
        ly.addView(t);

        Intent bat = registerReceiver(null, new IntentFilter(Intent.ACTION_BATTERY_CHANGED));
        int lvl = bat.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
        TextView st = new TextView(this);
        st.setText("\n● STATUS ENERGÉTICO: " + lvl + "%");
        st.setTextColor(Color.GREEN);
        ly.addView(st);

        setContentView(ly);
    }
}
