# Generated by Django 5.0.6 on 2024-05-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_produtos', '0002_rename_id_usuario_produto_id_produto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.TextField(default='', max_length=255),
        ),
    ]
