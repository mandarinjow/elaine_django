# Generated by Django 3.1 on 2020-08-10 15:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0010_auto_20200810_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualInspection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('validity_start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('validity_end_date', models.DateField(null=True, verbose_name='Expiry Date')),
                ('validity', models.BooleanField(default=True, help_text='Is the inspection valid?', verbose_name='Inspection Valid')),
                ('in_use', models.BooleanField(default=True, help_text='Is the inspection in use?', verbose_name='Inspection In Use')),
                ('type', models.CharField(choices=[('s', 'Sling'), ('k', 'Skid')], default='k', help_text='Type of Item', max_length=1)),
                ('material_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.instance', verbose_name='Instance S/N')),
            ],
            options={
                'verbose_name_plural': 'Visual Inspections',
            },
        ),
        migrations.CreateModel(
            name='MPIInpection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('validity_start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('validity_end_date', models.DateField(null=True, verbose_name='Expiry Date')),
                ('validity', models.BooleanField(default=True, help_text='Is the inspection valid?', verbose_name='Inspection Valid')),
                ('in_use', models.BooleanField(default=True, help_text='Is the inspection in use?', verbose_name='Inspection In Use')),
                ('type', models.CharField(choices=[('s', 'Sling'), ('k', 'Skid')], default='k', help_text='Type of Item', max_length=1)),
                ('material_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.instance', verbose_name='Instance S/N')),
            ],
            options={
                'verbose_name_plural': 'MPI Inspections',
            },
        ),
        migrations.CreateModel(
            name='CalibrationInspection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('validity_start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('validity_end_date', models.DateField(null=True, verbose_name='Expiry Date')),
                ('validity', models.BooleanField(default=True, help_text='Is the inspection valid?', verbose_name='Inspection Valid')),
                ('in_use', models.BooleanField(default=True, help_text='Is the inspection in use?', verbose_name='Inspection In Use')),
                ('material_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.instance', verbose_name='Instance S/N')),
            ],
            options={
                'verbose_name': 'Calibration Inspection',
            },
        ),
    ]
