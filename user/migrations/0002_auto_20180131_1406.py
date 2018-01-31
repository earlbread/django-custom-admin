# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailChangeRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('new_email', models.CharField(max_length=255)),
                ('id_card', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserForChangingEmail',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('user.user',),
        ),
        migrations.AddField(
            model_name='emailchangerequest',
            name='user',
            field=models.OneToOneField(to='user.UserForChangingEmail'),
        ),
    ]
