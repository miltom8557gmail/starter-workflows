package com.akame.portal;
import android.util.Log;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class AkameCloudConnector {
    // Aponta para o IP da sua Supermáquina (Termux local ou Cloud via SSH Tunnel)
    private static final String SERVER_URL = "http://127.0.0.1:8080/command";
    
    public static void sendCommand(String command) {
        new Thread(() -> {
            try {
                URL url = new URL(SERVER_URL);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");
                conn.setDoOutput(true);
                conn.getOutputStream().write(("cmd=" + command).getBytes());
                Log.d("AKAME_REMOTE", "Sinal enviado à Supermáquina: " + command);
            } catch (Exception e) {
                Log.e("AKAME_REMOTE", "Falha na ponte: " + e.getMessage());
            }
        }).start();
    }
}
