# Generated by Django 3.2.18 on 2023-03-04 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uaa', '0005_profile_department'),
        ('workOrder', '0003_maintenanceschedule_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenanceschedule',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='department_maintenanceSchedule', to='uaa.department'),
        ),
    ]
