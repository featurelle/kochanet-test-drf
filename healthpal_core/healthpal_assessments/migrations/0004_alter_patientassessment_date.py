# Generated by Django 5.1.1 on 2024-09-24 14:11

import datetime
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpal_assessments', '0003_alter_patientassessment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientassessment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2024, 9, 24), message='Assessment date cannot be in the future.')]),
        ),
    ]
