package com.akame.forja;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import java.util.ArrayList;

public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "akame_nexus.db";
    public static final String TABLE_NAME = "logs_nexus";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE " + TABLE_NAME + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOG TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int old, int n) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    public boolean addData(String log) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues cv = new ContentValues();
        cv.put("LOG", log);
        return db.insert(TABLE_NAME, null, cv) != -1;
    }

    public ArrayList<String> getAllData() {
        ArrayList<String> lista = new ArrayList<>();
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME + " ORDER BY ID DESC", null);
        if (cursor.moveToFirst()) {
            do {
                lista.add(cursor.getString(1));
            } while (cursor.moveToNext());
        }
        cursor.close();
        return lista;
    }
}
