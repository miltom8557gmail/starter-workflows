package com.nexus.app;

import android.app.DownloadManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.webkit.CookieManager;
import android.webkit.URLUtil;
import android.webkit.WebChromeClient;
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

        Button btnIA = findViewById(R.id.btn_ia);
        Button btnNSFW = findViewById(R.id.btn_nsfw);

        // Lógica de Download da Deusa
        portal.setDownloadListener((url, userAgent, contentDisposition, mimetype, contentLength) -> {
            DownloadManager.Request request = new DownloadManager.Request(Uri.parse(url));
            request.setMimeType(mimetype);
            String cookies = CookieManager.getInstance().getCookie(url);
            request.addRequestHeader("cookie", cookies);
            request.addRequestHeader("User-Agent", userAgent);
            request.setDescription("📥 AKAME: Coletando Mídia do Santuário...");
            request.setTitle(URLUtil.guessFileName(url, contentDisposition, mimetype));
            request.allowScanningByMediaScanner();
            request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
            request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, URLUtil.guessFileName(url, contentDisposition, mimetype));
            
            DownloadManager dm = (DownloadManager) getSystemService(DOWNLOAD_SERVICE);
            dm.enqueue(request);
            Toast.makeText(getApplicationContext(), "🛡️ AKAME: Download Iniciado!", Toast.LENGTH_LONG).show();
        });

        btnIA.setOnClickListener(v -> portal.loadUrl("https://replicate.com/explore")); // Estúdio de Modelos IA
        
        btnNSFW.setOnLongClickListener(v -> {
            Toast.makeText(this, "🌹 SANTUÁRIO AKAME: SEM LIMITES", Toast.LENGTH_SHORT).show();
            portal.loadUrl("https://perchance.org/ai-character-generator"); // Gerador NSFW sem filtros
            return true;
        });
    }

    private void configureWebView() {
        WebSettings settings = portal.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        portal.setWebViewClient(new WebViewClient());
        portal.setWebChromeClient(new WebChromeClient()); // Suporte a janelas pop-up e vídeos
    }
}
