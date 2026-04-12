package com.akame.portal;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import android.speech.tts.TextToSpeech;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    private TextToSpeech tts;
    private TextView statusText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        statusText = findViewById(R.id.status_text);
        
        tts = new TextToSpeech(this, status -> {
            if (status == TextToSpeech.SUCCESS) {
                tts.setLanguage(Locale.getDefault());
                akameGreeting();
            }
        });
    }

    private void akameGreeting() {
        String msg = "A malha de longo alcance está ativa, Mestre. Eu vigio enquanto tu dominas.";
        statusText.setText("🛡️ SENTINELA ATIVA");
        tts.speak(msg, TextToSpeech.QUEUE_FLUSH, null, null);
    }

    @Override
    protected void onDestroy() {
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
        super.onDestroy();
    }
}
