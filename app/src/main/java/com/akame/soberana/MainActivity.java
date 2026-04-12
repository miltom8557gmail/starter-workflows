package com.akame.soberana;
import android.app.Activity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Button btn = findViewById(R.id.btnVitrine);
        btn.setOnClickListener(v -> Toast.makeText(this, "📡 Conectando à Vitrine Soberana...", Toast.LENGTH_SHORT).show());
    }
}
