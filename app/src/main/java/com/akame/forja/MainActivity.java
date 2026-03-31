package com.akame.forja;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.tabs.TabLayout;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private DatabaseHelper dbHelper;
    private View pinScreen, mainContent, cardPersonagem, chatInterface, dashScroll;
    private EditText etPin, etMsg;
    private TextView chatLog, abaTitulo;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DatabaseHelper(this);
        pinScreen = findViewById(R.id.pin_screen);
        mainContent = findViewById(R.id.main_content);
        chatInterface = findViewById(R.id.chat_interface);
        dashScroll = findViewById(R.id.dashboard_scroll);
        cardPersonagem = findViewById(R.id.card_personagem);
        etPin = findViewById(R.id.et_pin_entry);
        etMsg = findViewById(R.id.et_message);
        chatLog = findViewById(R.id.chat_log);
        abaTitulo = findViewById(R.id.aba_titulo);
        listView = findViewById(R.id.listView_logs);

        TabLayout tabLayout = findViewById(R.id.tab_layout);
        tabLayout.addTab(tabLayout.newTab().setText("Explorar"));
        tabLayout.addTab(tabLayout.newTab().setText("Reveri"));
        tabLayout.addTab(tabLayout.newTab().setText("Sistema"));

        tabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) { mudarAba(tab.getPosition()); }
            @Override public void onTabUnselected(TabLayout.Tab tab) {}
            @Override public void onTabReselected(TabLayout.Tab tab) {}
        });

        // DESBLOQUEIO PIN 3650 / MILTON
        findViewById(R.id.btn_unlock).setOnClickListener(v -> {
            String pass = etPin.getText().toString();
            if (pass.equals("3650") || pass.equalsIgnoreCase("Milton")) {
                pinScreen.setVisibility(View.GONE);
                mainContent.setVisibility(View.VISIBLE);
                dbHelper.addData("NUCLEO: Acesso garantido (" + pass + ")");
            } else { Toast.makeText(this, "PIN INVÁLIDO", Toast.LENGTH_SHORT).show(); }
        });

        // LÓGICA DE CHAT
        findViewById(R.id.btn_interagir).setOnClickListener(v -> {
            dashScroll.setVisibility(View.GONE);
            chatInterface.setVisibility(View.VISIBLE);
        });

        findViewById(R.id.btn_close_chat).setOnClickListener(v -> {
            chatInterface.setVisibility(View.GONE);
            dashScroll.setVisibility(View.VISIBLE);
        });

        findViewById(R.id.btn_send).setOnClickListener(v -> {
            String msg = etMsg.getText().toString();
            if (!msg.isEmpty()) {
                chatLog.append("Tu: " + msg + "\n");
                chatLog.append("Seraphina: [Digitando...] (Conexão via Nexus estabelecida)\n\n");
                etMsg.setText("");
                dbHelper.addData("ROLEPLAY: Mensagem enviada.");
            }
        });

        atualizarLista();
    }

    private void mudarAba(int pos) {
        chatInterface.setVisibility(View.GONE);
        dashScroll.setVisibility(View.VISIBLE);
        if (pos == 0) {
            abaTitulo.setText("DESCOBRIR PERSONAGENS");
            cardPersonagem.setVisibility(View.VISIBLE);
            listView.setVisibility(View.GONE);
        } else if (pos == 1) {
            abaTitulo.setText("REVERI: FOCO SUPREMO");
            cardPersonagem.setVisibility(View.GONE);
            listView.setVisibility(View.VISIBLE);
            dbHelper.addData("REVERI: Módulo de hipnose carregado.");
        } else {
            abaTitulo.setText("LOGS DO IMPÉRIO");
            cardPersonagem.setVisibility(View.GONE);
            listView.setVisibility(View.VISIBLE);
        }
        atualizarLista();
    }

    private void atualizarLista() {
        ArrayList<String> logs = dbHelper.getAllData();
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, logs);
        listView.setAdapter(adapter);
    }
}
