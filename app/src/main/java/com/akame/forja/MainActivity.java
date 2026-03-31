package com.akame.forja;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.tabs.TabLayout;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private View pinScreen, mainContent;
    private EditText etPin;
    private TextView abaTitulo;
    private Button btnAcao;
    private ListView listView;
    private static final int PICK_IMAGE_REQUEST = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        pinScreen = findViewById(R.id.pin_screen);
        mainContent = findViewById(R.id.main_content);
        etPin = findViewById(R.id.et_pin_entry);
        abaTitulo = findViewById(R.id.aba_titulo);
        btnAcao = findViewById(R.id.btn_acao_principal);
        listView = findViewById(R.id.listView_logs);

        // CONFIGURAÇÃO DAS ABAS ESTILO REVERI
        TabLayout tabLayout = findViewById(R.id.tab_layout);
        tabLayout.addTab(tabLayout.newTab().setText("Segurança"));
        tabLayout.addTab(tabLayout.newTab().setText("Reveri"));
        tabLayout.addTab(tabLayout.newTab().setText("Logs"));

        tabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                mudarAba(tab.getPosition());
            }
            @Override public void onTabUnselected(TabLayout.Tab tab) {}
            @Override public void onTabReselected(TabLayout.Tab tab) {}
        });

        // BOTÃO DE DESBLOQUEIO (PIN 3650 OU MILTON)
        findViewById(R.id.btn_unlock).setOnClickListener(v -> {
            String pass = etPin.getText().toString();
            if (pass.equals("3650") || pass.equalsIgnoreCase("Milton")) {
                pinScreen.setVisibility(View.GONE);
                mainContent.setVisibility(View.VISIBLE);
                dbHelper.addData("ACESSO: " + pass + " autenticado.");
                atualizarLista();
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });

        btnAcao.setOnClickListener(v -> {
            if (btnAcao.getText().toString().contains("REVERI")) {
                dbHelper.addData("REVERI: Iniciando ciclo de Foco.");
                Toast.makeText(this, "Concentração iniciada...", Toast.LENGTH_SHORT).show();
            } else {
                Intent intent = new Intent(Intent.ACTION_PICK);
                intent.setType("image/*");
                startActivityForResult(intent, PICK_IMAGE_REQUEST);
            }
            atualizarLista();
        });

        atualizarLista();
    }

    private void mudarAba(int posicao) {
        if (posicao == 0) {
            abaTitulo.setText("SEGURANÇA ATIVA");
            btnAcao.setText("🛡️ LIMPAR EXIF (GALERIA)");
            btnAcao.setBackgroundColor(0xFFFFD700);
        } else if (posicao == 1) {
            abaTitulo.setText("REVERI: AUTO-HIPNOSE");
            btnAcao.setText("🧘 INICIAR SESSÃO REVERI");
            btnAcao.setBackgroundColor(0xFF6200EE);
        } else {
            abaTitulo.setText("HISTÓRICO DE LOGS");
            btnAcao.setText("LIMPAR TUDO");
            btnAcao.setBackgroundColor(0xFF444444);
        }
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
