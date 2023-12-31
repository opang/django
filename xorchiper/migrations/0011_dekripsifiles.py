# Generated by Django 4.2.2 on 2023-06-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xorchiper', '0010_alter_enkripsifiles_fi'),
    ]

    operations = [
        migrations.CreateModel(
            name='DekripsiFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(blank=True, max_length=255)),
                ('fi', models.FileField(blank=True, upload_to='')),
                ('encrypted_by', models.CharField(blank=True, max_length=50)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
