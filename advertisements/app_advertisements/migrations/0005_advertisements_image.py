# Generated by Django 4.2.5 on 2023-09-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_alter_advertisements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
