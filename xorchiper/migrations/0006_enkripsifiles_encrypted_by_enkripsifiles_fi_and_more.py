# Generated by Django 4.2.2 on 2023-06-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0005_alter_enkripsifiles_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='enkripsifiles',
            name='encrypted_by',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='enkripsifiles',
            name='fi',
            field=models.FileField(blank=True, upload_to='media/encryptedFiles'),
        ),
        migrations.AddField(
            model_name='enkripsifiles',
            name='size',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
