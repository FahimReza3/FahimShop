# Generated by Django 5.0.4 on 2024-07-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_alter_profile_melicode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_caart',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
