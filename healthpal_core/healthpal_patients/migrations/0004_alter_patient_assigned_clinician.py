# Generated by Django 5.1.1 on 2024-09-23 13:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpal_patients', '0003_patient_assigned_clinician_alter_patient_address_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assigned_clinician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_patients', to=settings.AUTH_USER_MODEL),
        ),
    ]
