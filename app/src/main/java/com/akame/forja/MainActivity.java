package com.akame.forja;
import android.os.Bundle;
import android.webkit.*;
import android.widget.*;
import android.net.Uri;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        WebView myWebView = findViewById(R.id.web_view);
        myWebView.setWebViewClient(new WebViewClient());
        myWebView.getSettings().setJavaScriptEnabled(true);
        myWebView.loadUrl("https://www.google.com");

        VideoView videoView = findViewById(R.id.video_player);
        Button btnDown = findViewById(R.id.btn_download);
        EditText urlIn = findViewById(R.id.url_input);

        btnDown.setOnClickListener(v -> {
            String url = urlIn.getText().toString();
            Toast.makeText(this, "Enviando " + url + " para o YT-DLP no GitHub...", Toast.LENGTH_LONG).show();
        });

        findViewById(R.id.btn_ubuntu).setOnClickListener(v -> {
            Toast.makeText(this, "Instanciando Ubuntu/Dolphin Open...", Toast.LENGTH_SHORT).show();
        });
    }
}
