# Generated by Django 3.0 on 2022-04-18 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220418_0559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
