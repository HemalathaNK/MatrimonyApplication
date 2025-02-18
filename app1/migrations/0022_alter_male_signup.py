# Generated by Django 4.2.14 on 2025-01-05 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0021_male_female"),
    ]

    operations = [
        migrations.AlterField(
            model_name="male",
            name="signup",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Signup",
                to="app1.signup",
            ),
        ),
    ]
