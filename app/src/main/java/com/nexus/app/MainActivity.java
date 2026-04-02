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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        portal = findViewById(R.id.portal_view);
        configureWebView();

        Button btnHome = findViewById(R.id.btn_home);
        Button btnIA = findViewById(R.id.btn_ia);
        Button btnNSFW = findViewById(R.id.btn_nsfw);

        // NAVEGAÇÃO DA DEUSA AKAME
        btnHome.setOnClickListener(v -> portal.loadUrl("about:blank"));
        
        btnIA.setOnClickListener(v -> {
            Toast.makeText(this, "AKAME: Ativando Núcleo Generativo...", Toast.LENGTH_SHORT).show();
            portal.loadUrl("https://www.bing.com/create"); // Placeholder para o Estúdio
        });

        btnNSFW.setOnClickListener(v -> {
            // Lógica de proteção: Um clique simples apenas avisa.
            Toast.makeText(this, "AKAME: O Santuário exige o selo de Mestre.", Toast.LENGTH_LONG).show();
        });
        
        // Clique longo no botão NSFW libera o portal oculto
        btnNSFW.setOnLongClickListener(v -> {
            Toast.makeText(this, "🌹 BEM-VINDO AO SANTUÁRIO SEM FILTROS", Toast.LENGTH_LONG).show();
            portal.loadUrl("https://civitai.com"); // Exemplo de acesso a modelos LoRA/NSFW
            return true;
        });
    }

    private void configureWebView() {
        WebSettings settings = portal.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        portal.setWebViewClient(new WebViewClient());
    }
}
