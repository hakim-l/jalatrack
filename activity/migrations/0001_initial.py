# Generated by Django 3.2 on 2023-10-14 07:30

from django.db import migrations, models
import django_spanner


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, unique=True)),
                ('started_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'activities',
            },
        ),
    ]