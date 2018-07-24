# Generated by Django 2.0.1 on 2018-01-30 04:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name for the media', max_length=100)),
                ('dateCreated', models.DateField(blank=True, null=True)),
                ('medType', models.CharField(choices=[('a', 'Agar'), ('w', 'Wort'), ('g', 'Glycerin'), ('sc', 'Sodium chloride'), ('g', 'Gelatine')], help_text='Select the appropriate media type', max_length=100)),
                ('volume', models.PositiveSmallIntegerField(help_text='Enter the total volume of media created', null=True)),
                ('gravity', models.PositiveSmallIntegerField(help_text='Enter the gravity of media created', null=True)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
            ],
            options={
                'ordering': ['dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceType', models.CharField(help_text='Enter or select the source of yeast (e.g. reculture of bottle, commercial yeast etc.)', max_length=100)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
            ],
            options={
                'ordering': ['sourceType'],
            },
        ),
        migrations.CreateModel(
            name='StorageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storageType', models.CharField(blank=True, choices=[('s', 'Slant'), ('p', 'Plate'), ('sol', 'Solution'), ('f', 'Freeze'), ('o', 'Other')], help_text='Select the appropriate yeast storage category', max_length=100)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Yeast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the yeast strain', max_length=100)),
                ('dateIsolated', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
                ('attenuation', models.PositiveSmallIntegerField(null=True)),
                ('flocculation', models.CharField(blank=True, choices=[('L', 'Low'), ('M', 'Moderate'), ('H', 'High')], help_text='Yeast flocculation', max_length=1)),
                ('tolerance', models.PositiveSmallIntegerField(null=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Source')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='YeastInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular yeast instance', primary_key=True, serialize=False)),
                ('dateCreated', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
                ('media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Media')),
                ('storageType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.StorageType')),
                ('yeast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Yeast')),
            ],
            options={
                'ordering': ['yeast', 'dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='YeastType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yeastType', models.CharField(help_text='Enter or select the type of yeast (e.g. lager, ale)', max_length=100)),
                ('comments', models.CharField(help_text='Enter comments (up to 255 characters)', max_length=255)),
            ],
            options={
                'ordering': ['yeastType'],
            },
        ),
        migrations.AddField(
            model_name='yeast',
            name='yeastType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.YeastType'),
        ),
    ]
