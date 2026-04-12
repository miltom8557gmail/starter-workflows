package com.akame.nexus;
import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.*;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        WebView v = new WebView(this);
        setContentView(v);
        v.getSettings().setJavaScriptEnabled(true);
        v.getSettings().setDomStorageEnabled(true);
        v.getSettings().setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        v.setWebViewClient(new WebViewClient());
        v.loadUrl("http://127.0.0.1:8080");
    }
}
