# Generated by Django 5.0.6 on 2024-05-22 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_usuario',
            new_name='id_produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='idade',
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
