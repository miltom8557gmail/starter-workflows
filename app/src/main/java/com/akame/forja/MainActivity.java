package com.akame.forja;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private View pinScreen, mainContent;
    private EditText etPin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        pinScreen = findViewById(R.id.pin_screen);
        mainContent = findViewById(R.id.main_content);
        etPin = findViewById(R.id.et_pin_entry);

        findViewById(R.id.btn_unlock).setOnClickListener(v -> {
            String entry = etPin.getText().toString();
            // Lógica: PIN 3650 ou Chave Mestra 'Milton'
            if (entry.equals("3650") || entry.equalsIgnoreCase("Milton")) {
                pinScreen.setVisibility(View.GONE);
                mainContent.setVisibility(View.VISIBLE);
                dbHelper.addData("ACESSO: Sistema liberado por " + entry);
            } else {
                Toast.makeText(this, "Acesso Negado", Toast.LENGTH_SHORT).show();
            }
        });

        findViewById(R.id.btn_reveri_tool).setOnClickListener(v -> {
            Toast.makeText(this, "Acessando Ferramentas Reveri...", Toast.LENGTH_SHORT).show();
            // A lógica de hipnose será injetada no Passo 3
        });

        atualizarLista();
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        ((ListView)findViewById(R.id.listView)).setAdapter(adapter);
    }
}
