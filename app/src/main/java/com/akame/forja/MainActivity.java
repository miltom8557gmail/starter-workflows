package com.akame.forja;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.tabs.TabLayout;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private View pinScreen, mainContent, cardPersonagem;
    private EditText etPin;
    private TextView abaTitulo;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        pinScreen = findViewById(R.id.pin_screen);
        mainContent = findViewById(R.id.main_content);
        cardPersonagem = findViewById(R.id.card_personagem);
        etPin = findViewById(R.id.et_pin_entry);
        abaTitulo = findViewById(R.id.aba_titulo);
        listView = findViewById(R.id.listView_logs);

        TabLayout tabLayout = findViewById(R.id.tab_layout);
        tabLayout.addTab(tabLayout.newTab().setText("Descobrir"));
        tabLayout.addTab(tabLayout.newTab().setText("Reveri"));
        tabLayout.addTab(tabLayout.newTab().setText("Segurança"));

        tabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) { mudarAba(tab.getPosition()); }
            @Override public void onTabUnselected(TabLayout.Tab tab) {}
            @Override public void onTabReselected(TabLayout.Tab tab) {}
        });

        findViewById(R.id.btn_unlock).setOnClickListener(v -> {
            String pass = etPin.getText().toString();
            if (pass.equals("3650") || pass.equalsIgnoreCase("Milton")) {
                pinScreen.setVisibility(View.GONE);
                mainContent.setVisibility(View.VISIBLE);
                dbHelper.addData("ACESSO: " + pass + " desbloqueou o Nexus.");
            } else {
                Toast.makeText(this, "ACESSO NEGADO", Toast.LENGTH_SHORT).show();
            }
        });

        findViewById(R.id.btn_interagir).setOnClickListener(v -> {
            dbHelper.addData("HISTÓRIA: Iniciando capítulo com Seraphina Vale.");
            Toast.makeText(this, "Entrando em modo narrativo...", Toast.LENGTH_LONG).show();
        });

        atualizarLista();
    }

    private void mudarAba(int posicao) {
        if (posicao == 0) { // Descobrir
            abaTitulo.setText("DESCOBRIR 18+");
            cardPersonagem.setVisibility(View.VISIBLE);
            listView.setVisibility(View.GONE);
        } else if (posicao == 1) { // Reveri
            abaTitulo.setText("REVERI: AUTO-HIPNOSE");
            cardPersonagem.setVisibility(View.GONE);
            listView.setVisibility(View.VISIBLE);
        } else { // Segurança
            abaTitulo.setText("LOGS DE SEGURANÇA");
            cardPersonagem.setVisibility(View.GONE);
            listView.setVisibility(View.VISIBLE);
        }
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
