package com.imperio.app;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText pinInput = findViewById(R.id.pinInput);
        Button btnEntrar = findViewById(R.id.btnEntrar);
        btnEntrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String pin = pinInput.getText().toString();
                if (pin.equals("3650") || pin.equalsIgnoreCase("Milton")) {
                    Toast.makeText(MainActivity.this, "ACESSO CONCEDIDO", Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(MainActivity.this, "PIN INCORRETO", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
