# Generated by Django 3.1 on 2020-08-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200810_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(help_text='Unique ID for Material Type', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('description', models.CharField(help_text='Type of Equipment', max_length=64, verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(choices=[('n', 'Not Ready'), ('w', 'Expiring'), ('r', 'Ready'), ('e', 'Expired')], default='n', help_text='Status of Item', max_length=1),
        ),
        migrations.AddField(
            model_name='material',
            name='material_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.materialtype', verbose_name='Equipment Type'),
        ),
    ]
