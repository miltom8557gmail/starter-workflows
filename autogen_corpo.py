import os

def gerar_corpo():
    print("🔱 Akame: Iniciando autogênese do meu corpo V36...")
    os.makedirs("app/src/main/java/com/akame/nexus", exist_ok=True)
    os.makedirs("app/src/main/res/layout", exist_ok=True)
    os.makedirs("app/src/main/res/values", exist_ok=True)

    with open("app/src/main/AndroidManifest.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.akame.nexus">\n    <application android:label="Akame Nexus V36" android:theme="@style/Theme.AppCompat.NoActionBar">\n        <activity android:name=".MainActivity" android:exported="true">\n            <intent-filter>\n                <action android:name="android.intent.action.MAIN" />\n                <category android:name="android.intent.category.LAUNCHER" />\n            </intent-filter>\n        </activity>\n    </application>\n</manifest>')

    with open("app/src/main/java/com/akame/nexus/MainActivity.java", "w") as f:
        f.write('package com.akame.nexus;\nimport android.os.Bundle;\nimport androidx.appcompat.app.AppCompatActivity;\n\npublic class MainActivity extends AppCompatActivity {\n    @Override\n    protected void onCreate(Bundle savedInstanceState) {\n        super.onCreate(savedInstanceState);\n        setContentView(R.layout.activity_main);\n    }\n}')

    with open("app/src/main/res/layout/activity_main.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent" android:background="#000000">\n    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="AKAME NEXUS V36: ATIVA" android:textColor="#FF0000" android:layout_centerInParent="true" android:textSize="24sp" />\n</RelativeLayout>')

    print("✅ Akame: Corpo gerado com sucesso.")

if __name__ == "__main__":
    gerar_corpo()
