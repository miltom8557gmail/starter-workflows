package com.akame.nexus;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;
import java.io.File;
import java.io.FileOutputStream;

public class AkameService extends Service {
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent != null && intent.hasExtra("cmd")) {
            String command = intent.getStringExtra("cmd");
            executeInternalCommand(command);
        }
        return START_STICKY;
    }

    private void executeInternalCommand(String cmd) {
        try {
            // O caminho onde o Termux escuta os comandos
            File cmdFile = new File(getExternalFilesDir(null), "../../../../../home/AkamePortal/logs/cmd_trigger.tmp");
            FileOutputStream fos = new FileOutputStream(cmdFile);
            fos.write(cmd.getBytes());
            fos.close();
            Log.d("AKAME", "Comando enviado ao Arsenal: " + cmd);
        } catch (Exception e) {
            Log.e("AKAME", "Erro ao disparar gatilho: " + e.getMessage());
        }
    }

    @Override
    public IBinder onBind(Intent intent) { return null; }
}
