# Generated by Django 2.0.1 on 2018-05-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180509_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='yeast',
            name='cetegory',
            field=models.CharField(blank=True, choices=[('Clean', 'Clean'), ('Fruity', 'Fruity'), ('Hybrid', 'Hybrid'), ('Phenolic', 'Phenolic'), ('Eccentric', 'Eccetric'), ('Dry', 'Dry'), ('Full', 'Full')], help_text='Yeast category', max_length=10),
        ),
    ]
