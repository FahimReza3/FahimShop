# Generated by Django 5.0.4 on 2024-06-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_profile_melicode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='meliCode',
            field=models.CharField(blank=True, default='0', max_length=10),
        ),
    ]
