package com.nexus.app;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private WebView portal;
    // IP PADRÃO DO TERMUX (Pode ser alterado para o seu IP real)
    private String termuxServer = "http://127.0.0.1:8080"; 

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        portal = findViewById(R.id.portal_view);
        configureWebView();

        Button btnIA = findViewById(R.id.btn_ia);
        Button btnHome = findViewById(R.id.btn_home);

        // COMANDO PARA CONECTAR AO LABORATORIO DO TERMUX
        btnIA.setOnClickListener(v -> {
            Toast.makeText(this, "AKAME: Conectando ao Núcleo Termux...", Toast.LENGTH_SHORT).show();
            portal.loadUrl(termuxServer); 
        });

        btnHome.setOnClickListener(v -> {
            portal.loadUrl("about:blank");
            Toast.makeText(this, "AKAME: Standby...", Toast.LENGTH_SHORT).show();
        });
    }

    private void configureWebView() {
        WebSettings settings = portal.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        portal.setWebViewClient(new WebViewClient());
    }
}
