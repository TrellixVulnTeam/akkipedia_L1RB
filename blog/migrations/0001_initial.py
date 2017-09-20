# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-20 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/%Y/%m')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True, db_index=True)),
                ('updateddate', models.DateTimeField(auto_now=True, db_index=True)),
                ('author', models.CharField(default='Admin', max_length=50)),
            ],
            options={
                'ordering': ['-id', 'date', '-updateddate'],
            },
        ),
    ]
