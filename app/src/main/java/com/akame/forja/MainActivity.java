package com.akame.forja;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private ProgressBar progressSync;
    private ListView listView;
    
    // ATENÇÃO: COLOQUE SEU TOKEN DO GITHUB AQUI PARA O APK FUNCIONAR
    private String GITHUB_TOKEN = "SEU_TOKEN_AQUI"; 
    private String REPO_OWNER = "SEU_USUARIO";
    private String REPO_NAME = "NOME_DO_REPO";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        progressSync = findViewById(R.id.progress_sync);
        listView = findViewById(R.id.listView);

        findViewById(R.id.btn_sync_cloud).setOnClickListener(v -> {
            executarSincronizacaoCloud();
        });

        atualizarLista();
    }

    private void executarSincronizacaoCloud() {
        progressSync.setVisibility(View.VISIBLE);
        dbHelper.addData("🛰️ CONECTANDO AO GITHUB API...");
        atualizarLista();

        new Thread(() -> {
            try {
                // Endpoint para criar/atualizar arquivo e disparar o Actions
                URL url = new URL("https://api.github.com/repos/" + REPO_OWNER + "/" + REPO_NAME + "/contents/trigger.txt");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("PUT");
                conn.setRequestProperty("Authorization", "token " + GITHUB_TOKEN);
                conn.setRequestProperty("Content-Type", "application/json");
                conn.setDoOutput(true);

                // JSON simples para atualizar o trigger
                String json = "{\"message\":\"Sync from App\", \"content\":\"YXV0b21hdGljX3N5bmNfYWthbWU=\", \"sha\":\"\"}";

                OutputStream os = conn.getOutputStream();
                os.write(json.getBytes());
                os.flush();
                os.close();

                int code = conn.getResponseCode();
                runOnUiThread(() -> {
                    progressSync.setVisibility(View.GONE);
                    if(code == 200 || code == 201) {
                        dbHelper.addData("✅ CLOUD: Sincronização disparada com sucesso!");
                        Toast.makeText(this, "Ordem enviada ao GitHub!", Toast.LENGTH_SHORT).show();
                    } else {
                        dbHelper.addData("❌ ERRO CLOUD: Código " + code);
                    }
                    atualizarLista();
                });
            } catch (Exception e) {
                runOnUiThread(() -> {
                    progressSync.setVisibility(View.GONE);
                    dbHelper.addData("❌ FALHA DE REDE: " + e.getMessage());
                    atualizarLista();
                });
            }
        }).start();
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
