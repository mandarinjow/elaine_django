# Generated by Django 3.1 on 2020-08-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200810_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(choices=[('n', 'Not Ready'), ('w', 'Expiring'), ('e', 'Expired'), ('r', 'Ready')], default='n', help_text='Status of Item', max_length=1),
        ),
    ]
