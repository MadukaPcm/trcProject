# Generated by Django 3.2.18 on 2023-03-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='categoryOne',
            new_name='categoryTwo',
        ),
        migrations.RemoveField(
            model_name='station',
            name='isStandard',
        ),
    ]