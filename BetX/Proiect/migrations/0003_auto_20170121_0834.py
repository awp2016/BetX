# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Proiect', '0002_signup_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commnent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pronostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proiect.Pronostic')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('pronostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proiect.Pronostic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_value', models.CharField(max_length=200)),
                ('pronostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proiect.Pronostic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='pronostic',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]