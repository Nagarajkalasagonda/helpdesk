# Generated by Django 2.2.4 on 2019-08-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequest', '0006_auto_20190831_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmaster',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Employee'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Allocate', 'Allocate'), ('Reject', 'Reject'), ('Close', 'Close')], default='New', max_length=20, null=True),
        ),
    ]
