# Generated by Django 4.2 on 2024-04-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeshub', '0010_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profilepic.jpeg', upload_to='profile_images'),
        ),
    ]
