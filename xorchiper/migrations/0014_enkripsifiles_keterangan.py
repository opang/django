# Generated by Django 4.2.2 on 2023-07-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0013_dekripsifiles_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='enkripsifiles',
            name='keterangan',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
