# Generated by Django 2.2.4 on 2019-08-31 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequest', '0009_ticket_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='assetrequest.EmployeType'),
        ),
    ]
