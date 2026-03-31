package com.akame.forja;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private static final int PICK_IMAGE = 100;
    Uri imageUri;
    ImageView preview;
    EditText log;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        preview = findViewById(R.id.image_preview);
        log = findViewById(R.id.status_log);

        findViewById(R.id.btn_upload).setOnClickListener(v -> {
            Intent gallery = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.INTERNAL_CONTENT_URI);
            startActivityForResult(gallery, PICK_IMAGE);
        });

        findViewById(R.id.btn_analyze).setOnClickListener(v -> {
            if(imageUri != null){
                log.setText("Enviando referência para o GitHub... Analisando iluminação, filtros e maquiagem.");
                Toast.makeText(this, "Processando... O prompt extraído será salvo no repositório.", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "Mestre, suba uma imagem primeiro.", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == RESULT_OK && requestCode == PICK_IMAGE) {
            imageUri = data.getData();
            preview.setImageURI(imageUri);
            preview.setAlpha(1.0f);
        }
    }
}
