# Generated by Django 5.0.6 on 2024-07-17 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolistAPI", "0009_alter_userprofile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="todoitem",
            name="important",
            field=models.BooleanField(default=False),
        ),
    ]
