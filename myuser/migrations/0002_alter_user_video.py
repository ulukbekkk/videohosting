# Generated by Django 4.0 on 2022-05-06 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='video.video'),
        ),
    ]