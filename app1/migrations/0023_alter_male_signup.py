# Generated by Django 4.2.14 on 2025-01-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0022_alter_male_signup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="male",
            name="signup",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app1.signup"
            ),
        ),
    ]
