# Generated by Django 4.2.2 on 2023-06-23 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0007_alter_enkripsifiles_fi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enkripsifiles',
            name='fi',
        ),
    ]