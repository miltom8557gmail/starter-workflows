package com.akame.forja;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import java.util.ArrayList;

public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "akame_final.db";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE logs (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOG TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int old, int n) {
        db.execSQL("DROP TABLE IF EXISTS logs");
        onCreate(db);
    }

    public void addData(String log) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues cv = new ContentValues();
        cv.put("LOG", log);
        db.insert("logs", null, cv);
    }

    public ArrayList<String> getAllData() {
        ArrayList<String> lista = new ArrayList<>();
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM logs ORDER BY ID DESC", null);
        if (cursor.moveToFirst()) {
            do { lista.add(cursor.getString(1)); } while (cursor.moveToNext());
        }
        cursor.close();
        return lista;
    }
}
