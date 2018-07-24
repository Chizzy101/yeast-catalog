# Generated by Django 2.0.1 on 2018-01-31 14:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_yeastinstance_yeaststatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular yeast instance', primary_key=True, serialize=False)),
                ('dateCreated', models.DateField(blank=True, null=True)),
                ('dateInoc', models.DateField(blank=True, null=True)),
                ('yeastStatus', models.CharField(choices=[('u', 'used'), ('i', 'inoculated'), ('a', 'available')], help_text='Select the appropriate media type', max_length=100)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
                ('media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Media')),
                ('storageType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.StorageType')),
                ('yeast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Yeast')),
            ],
            options={
                'ordering': ['yeast', 'dateCreated'],
            },
        ),
        migrations.RemoveField(
            model_name='yeastinstance',
            name='media',
        ),
        migrations.RemoveField(
            model_name='yeastinstance',
            name='storageType',
        ),
        migrations.RemoveField(
            model_name='yeastinstance',
            name='yeast',
        ),
        migrations.DeleteModel(
            name='YeastInstance',
        ),
    ]
