# Generated by Django 3.2 on 2023-10-14 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employeemodel_division_id'),
        ('plan', '0002_rename_plans_planmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='planmodel',
            name='activity',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planmodel',
            name='activity_type',
            field=models.CharField(default='daily', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planmodel',
            name='employee_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='employee.employeemodel'),
            preserve_default=False,
        ),
    ]