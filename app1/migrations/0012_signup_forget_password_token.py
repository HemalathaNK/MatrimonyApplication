# Generated by Django 4.2.14 on 2025-01-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0011_alter_signup_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="signup",
            name="forget_password_token",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
