# Generated by Django 5.0.3 on 2024-03-22 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('person_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.personmodel')),
            ],
            options={
                'db_table': 'persondetail',
            },
        ),
    ]