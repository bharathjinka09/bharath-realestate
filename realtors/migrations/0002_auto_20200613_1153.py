# Generated by Django 2.2.12 on 2020-06-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]