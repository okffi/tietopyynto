# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150729_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_expert',
            field=models.BooleanField(default=False, help_text='Unlocks shortcuts and other experienced user features', verbose_name='Expert'),
        ),
    ]
