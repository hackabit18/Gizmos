package com.example.abhinav.bit;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Main3Activity extends AppCompatActivity {
    Intent intent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        intent= new Intent(Main3Activity.this, Main2Activity.class);
    }

    public void webp(View view) {
        startActivity(intent);
    }
}
