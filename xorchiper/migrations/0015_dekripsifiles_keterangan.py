# Generated by Django 4.2.2 on 2023-07-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0014_enkripsifiles_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='dekripsifiles',
            name='keterangan',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
