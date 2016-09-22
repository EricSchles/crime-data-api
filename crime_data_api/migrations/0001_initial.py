# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyOri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('city', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Circumstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeOriYearly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('is_nibrs_summary', models.BooleanField()),
                ('agency_ori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.AgencyOri')),
                ('count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.CrimeCount')),
            ],
        ),
        migrations.CreateModel(
            name='CrimeStateYearly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.CrimeCount')),
            ],
        ),
        migrations.CreateModel(
            name='CrimeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_of_day_gmt', models.IntegerField(default=0)),
                ('completed', models.BooleanField()),
                ('agency_ori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.AgencyOri')),
                ('circumstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.Circumstance')),
                ('clearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.Clearance')),
                ('crime_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.CrimeType')),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OffenseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OffenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
                ('offense_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.OffenseClass')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sex', models.CharField(max_length=128, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.Race'),
        ),
        migrations.AddField(
            model_name='incident',
            name='location_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.LocationType'),
        ),
        migrations.AddField(
            model_name='incident',
            name='offender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='crime_data_api.Person'),
        ),
        migrations.AddField(
            model_name='incident',
            name='offense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.OffenseType'),
        ),
        migrations.AddField(
            model_name='incident',
            name='relationship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.Relationship'),
        ),
        migrations.AddField(
            model_name='incident',
            name='victim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='crime_data_api.Person'),
        ),
        migrations.AddField(
            model_name='incident',
            name='weapon_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.WeaponType'),
        ),
        migrations.AddField(
            model_name='crimestateyearly',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.State'),
        ),
        migrations.AddField(
            model_name='crimecount',
            name='offense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.OffenseType'),
        ),
        migrations.AddField(
            model_name='agencyori',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.County'),
        ),
        migrations.AddField(
            model_name='agencyori',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_data_api.State'),
        ),
        migrations.AlterUniqueTogether(
            name='crimestateyearly',
            unique_together=set([('year', 'state')]),
        ),
        migrations.AlterUniqueTogether(
            name='crimeoriyearly',
            unique_together=set([('year', 'agency_ori')]),
        ),
    ]
