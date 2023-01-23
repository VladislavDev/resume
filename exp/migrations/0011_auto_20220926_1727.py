# Generated by Django 3.2.9 on 2022-09-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0010_delete_multilinguality'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyskill',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='keyskill',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='keysubskill',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='keysubskill',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]