# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpr', models.CharField(max_length=5)),
                ('wet', models.CharField(max_length=5)),
                ('ur', models.CharField(max_length=5)),
                ('li', models.CharField(max_length=5)),
            ],
        ),
    ]
