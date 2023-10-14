# Generated by Django 3.2 on 2023-10-14 09:04

from django.db import migrations, models
import django.db.models.deletion
import django_spanner


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityModel',
            fields=[
                ('id', models.AutoField(default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, unique=True)),
                ('end_at', models.DateTimeField()),
                ('activity', models.CharField(max_length=255)),
                # ('plan_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.planmodel')),
            ],
            options={
                'db_table': 'activities',
            },
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]