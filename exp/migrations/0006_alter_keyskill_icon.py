# Generated by Django 3.2.9 on 2022-09-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0005_auto_20220913_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyskill',
            name='icon',
            field=models.ImageField(upload_to='tech-icons'),
        ),
    ]