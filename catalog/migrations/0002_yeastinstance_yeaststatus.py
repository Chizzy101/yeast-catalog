# Generated by Django 2.0.1 on 2018-01-31 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yeastinstance',
            name='yeastStatus',
            field=models.CharField(choices=[('u', 'used'), ('a', 'available')], default='a', help_text='Select the appropriate media type', max_length=100),
            preserve_default=False,
        ),
    ]
