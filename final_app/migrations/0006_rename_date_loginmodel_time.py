# Generated by Django 4.1 on 2022-09-14 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("final_app", "0005_alter_loginmodel_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loginmodel", old_name="date", new_name="time",
        ),
    ]