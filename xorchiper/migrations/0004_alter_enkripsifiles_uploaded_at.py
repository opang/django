# Generated by Django 4.2.2 on 2023-06-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0003_alter_enkripsifiles_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enkripsifiles',
            name='uploaded_at',
            field=models.DateField(),
        ),
    ]
