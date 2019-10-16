# Generated by Django 2.2.4 on 2019-08-31 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequest', '0004_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='department',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='location',
        ),
        migrations.AddField(
            model_name='ticket',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Employee'),
        ),
    ]