package com.example.acer.camera;

import android.content.Intent;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;
import android.provider.SyncStateContract;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.view.View;
import android.widget.Toast;

import java.io.File;
import java.util.Date;

public class CameraActivity extends AppCompatActivity {
private  static final int ACTIVITY_START_CAMERAAPP=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
    }
    public void takePhoto(View view)
    {

        Intent callCameraApplicationIntent=new Intent();
        callCameraApplicationIntent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(callCameraApplicationIntent,ACTIVITY_START_CAMERAAPP);

    }
    protected void onActivityResult(int requestCode,int resultCode,Intent data)
    {
if(requestCode==ACTIVITY_START_CAMERAAPP&& resultCode==RESULT_OK)
    Toast.makeText(this,"picture taken",Toast.LENGTH_SHORT).show();

    }
}
