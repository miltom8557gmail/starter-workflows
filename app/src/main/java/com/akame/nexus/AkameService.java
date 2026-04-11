package com.akame.nexus;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import androidx.core.app.NotificationCompat;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.os.Build;
import android.util.Log;

public class AkameService extends Service {
    private static final String TAG = "AKAME_CORE";

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        createNotificationChannel();
        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "AKAME_CHANNEL")
                .setSmallIcon(android.R.drawable.ic_menu_compass)
                .setContentTitle("Akame Nexus")
                .setContentText("Ponte de Dados Ativa")
                .setPriority(NotificationCompat.PRIORITY_LOW);

        startForeground(1, builder.build());
        
        Log.d(TAG, "📡 Sincronizando com Bunker_Onion...");
        return START_STICKY;
    }

    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel serviceChannel = new NotificationChannel(
                    "AKAME_CHANNEL",
                    "Akame Service Channel",
                    NotificationManager.IMPORTANCE_DEFAULT
            );
            NotificationManager manager = getSystemService(NotificationManager.class);
            manager.createNotificationChannel(serviceChannel);
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
