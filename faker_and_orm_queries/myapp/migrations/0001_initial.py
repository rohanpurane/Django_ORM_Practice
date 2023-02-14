# Generated by Django 4.0.5 on 2022-12-24 09:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software_Hub',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_job_roll', models.CharField(max_length=100)),
                ('employee_salary', models.IntegerField()),
                ('employee_age', models.IntegerField()),
            ],
        ),
    ]
