# Generated by Django 4.2.18 on 2025-02-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_signup_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='video',
            field=models.FileField(null=True, upload_to='video/'),
        ),
    ]
