# Generated by Django 5.1.1 on 2024-09-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpal_assessments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientassessment',
            name='datetime',
        ),
        migrations.AddField(
            model_name='patientassessment',
            name='date',
            field=models.DateField(default='2020-10-10'),
            preserve_default=False,
        ),
    ]
