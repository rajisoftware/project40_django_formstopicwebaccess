# Generated by Django 4.1.7 on 2023-04-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webpage",
            name="mail",
        ),
        migrations.AddField(
            model_name="webpage",
            name="email",
            field=models.EmailField(default="cricketgmail.com", max_length=254),
        ),
    ]
