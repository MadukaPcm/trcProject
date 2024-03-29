# Generated by Django 3.2.18 on 2023-03-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20230306_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='costSpent',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='description',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='userManual',
        ),
        migrations.AddField(
            model_name='asset',
            name='lastMaintained',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='iam',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='orderStatus',
            field=models.BooleanField(default=True),
        ),
    ]
