# Generated by Django 4.1.7 on 2023-03-26 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_rename_tip_this_puzzle_tip_next'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='tip_next',
            new_name='tip_this',
        ),
    ]
