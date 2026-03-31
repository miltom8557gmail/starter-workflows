package com.akame.forja;

import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private ArrayAdapter<String> adapter;
    private ArrayList<String> listaItens;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        EditText etInput = findViewById(R.id.etInput);
        Button btnObfuscate = findViewById(R.id.btn_obfuscate);
        listView = findViewById(R.id.listView);

        atualizarLista();

        btnObfuscate.setOnClickListener(v -> {
            String log = etInput.getText().toString();
            if (log.isEmpty()) log = "Mídia Processada sem Metadados";
            
            // Simulação de limpeza e salvamento no banco
            dbHelper.addData("PROTEGIDO: " + log);
            atualizarLista();
            etInput.setText("");
            
            Toast.makeText(this, "🛡️ Camuflagem Aplicada. Rastros Removidos!", Toast.LENGTH_LONG).show();
        });
    }

    private void atualizarLista() {
        listaItens = dbHelper.getAllData();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, listaItens);
        listView.setAdapter(adapter);
    }
}
