# Generated by Django 3.2.9 on 2022-09-13 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0003_auto_20220913_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyskill',
            old_name='keyskill_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='keysubskill',
            old_name='keysubskill_text',
            new_name='name',
        ),
    ]
