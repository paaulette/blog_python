# Generated by Django 4.1.5 on 2023-05-22 17:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]