# Generated by Django 3.2.18 on 2023-03-30 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaa', '0005_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileImage',
            field=models.FileField(blank=True, default='profileImages/profile_default.png', null=True, upload_to='profileImages/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
    ]