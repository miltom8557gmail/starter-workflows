package com.akame.soberana;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Button btnVitrine = findViewById(R.id.btnVitrine);
        btnVitrine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "🌌 Abrindo Vitrine Remota...", Toast.LENGTH_LONG).show();
            }
        });
    }
}
