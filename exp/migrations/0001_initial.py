# Generated by Django 3.2.9 on 2022-09-13 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iconName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KeySubSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iconName', models.CharField(max_length=100)),
                ('key_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.keyskill')),
            ],
        ),
    ]