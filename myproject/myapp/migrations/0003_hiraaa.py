# Generated by Django 5.1 on 2024-08-25 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_pdata_age_alter_pdata_bed_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiraaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pdata', to='myapp.pdata')),
            ],
        ),
    ]
