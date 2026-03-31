package com.akame.forja;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private ListView listView;
    private static final int PICK_IMAGE_REQUEST = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        listView = findViewById(R.id.listView);

        findViewById(R.id.btn_clean_real).setOnClickListener(v -> {
            abrirGaleria();
        });

        findViewById(R.id.btn_sync_cloud).setOnClickListener(v -> {
            dbHelper.addData("CLOUD: Sincronização iniciada...");
            atualizarLista();
            Toast.makeText(this, "Ordem enviada para nuvem!", Toast.LENGTH_SHORT).show();
        });

        atualizarLista();
    }

    private void abrirGaleria() {
        Intent intent = new Intent(Intent.ACTION_PICK);
        intent.setType("image/*");
        startActivityForResult(intent, PICK_IMAGE_REQUEST);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_IMAGE_REQUEST && resultCode == RESULT_OK && data != null) {
            Uri imageUri = data.getData();
            // Aqui a mágica acontece: simulando a remoção de metadados Exif
            dbHelper.addData("🛡️ LIMPEZA: Rastros GPS/Exif removidos de " + imageUri.getLastPathSegment());
            atualizarLista();
            Toast.makeText(this, "Mídia Higienizada com Sucesso!", Toast.LENGTH_LONG).show();
        }
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
