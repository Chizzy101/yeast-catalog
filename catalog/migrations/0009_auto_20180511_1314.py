# Generated by Django 2.0.1 on 2018-05-11 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180511_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storageinstance',
            options={'ordering': ['date_created', 'id']},
        ),
    ]
