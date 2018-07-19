# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='messagepuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermessages', to='wall_app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentpmessage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagecomments', to='wall_app.Message'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentpuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercomments', to='wall_app.User'),
        ),
    ]
