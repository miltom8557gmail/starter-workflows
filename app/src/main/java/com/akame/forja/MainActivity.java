package com.akame.forja;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Spinner spinner = findViewById(R.id.spinner_personality);
        ArrayList<String> list = new ArrayList<>();
        list.add("Provocante (Seducer)");
        list.add("Analítica (Genius)");
        list.add("Caótica (Harley)");
        list.add("Doce (Waifu)");
        
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, list);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        findViewById(R.id.btn_lipsync).setOnClickListener(v -> {
            Toast.makeText(this, "Processando Wav2Lip no GitHub...", Toast.LENGTH_SHORT).show();
        });

        findViewById(R.id.btn_start_live).setOnClickListener(v -> {
            String p = spinner.getSelectedItem().toString();
            Toast.makeText(this, "Live Iniciada com Persona: " + p, Toast.LENGTH_LONG).show();
        });
    }
}
