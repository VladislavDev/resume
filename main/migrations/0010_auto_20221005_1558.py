# Generated by Django 3.2.9 on 2022-10-05 08:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20221005_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
