# Generated by Django 3.1 on 2020-08-10 02:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='Manufacturing Serial Number', max_length=64, verbose_name='Mfg S/N')),
                ('status', models.CharField(choices=[('n', 'Not Ready'), ('r', 'Ready'), ('e', 'Expired')], default='n', help_text='Status of Item', max_length=1)),
                ('instance_allocation', models.CharField(choices=[('w', 'West Pumping'), ('p', 'Plug & Abandonment'), ('h', 'Hydraulic WorkOver')], help_text='Item Allocated to which project', max_length=1, null=True)),
                ('instance_remarks', models.CharField(default='', help_text='Additional Comments', max_length=255, null=True, verbose_name='Additional Remarks')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('hal_number', models.IntegerField(help_text='SAP Number used by Halliburton Internal', primary_key=True, serialize=False, unique=True, verbose_name='HAL SAP Number')),
                ('hal_description', models.CharField(help_text='Description of Material', max_length=255, verbose_name='Description')),
                ('hal_old_number', models.CharField(help_text='Old Material number used by Halliburton Internal', max_length=64, verbose_name='HAL Old Mtl Number')),
            ],
        ),
        migrations.CreateModel(
            name='NDECertificate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('certificate_number', models.CharField(help_text='Certificate Number', max_length=255, verbose_name='Cert. Number')),
                ('validity_start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('validity_end_date', models.DateField(null=True, verbose_name='Expiry Date')),
                ('material_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.instance')),
            ],
        ),
        migrations.AddField(
            model_name='instance',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.material', verbose_name='Material Item'),
        ),
    ]
