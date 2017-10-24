# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-24 05:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hackers.Application')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('A', 'Accepted'), ('R', 'Rejected'), ('V', 'Ticket validated'), ('X', 'Expired'), ('FV', 'Friend validated'), ('NC', 'Needs change')], default='D', max_length=2)),
                ('assigned_money', models.FloatField(blank=True, null=True)),
                ('currency_sign', models.CharField(max_length=3)),
                ('paypal_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('origin_city', models.CharField(max_length=300)),
                ('origin_country', models.CharField(max_length=300)),
                ('expiration_time', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('change_reason', models.CharField(blank=True, max_length=300, null=True)),
                ('reimbursed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
