# Generated by Django 5.0.6 on 2024-06-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
