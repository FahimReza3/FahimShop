# Generated by Django 5.0.4 on 2024-07-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_profile_old_caart'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_caart2',
            field=models.CharField(default='1', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='old_caart',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
