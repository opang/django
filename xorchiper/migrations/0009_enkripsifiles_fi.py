# Generated by Django 4.2.2 on 2023-06-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0008_remove_enkripsifiles_fi'),
    ]

    operations = [
        migrations.AddField(
            model_name='enkripsifiles',
            name='fi',
            field=models.FileField(blank=True, upload_to='encryptedFiles'),
        ),
    ]
