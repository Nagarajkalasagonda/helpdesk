# Generated by Django 2.2.4 on 2019-08-31 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequest', '0002_auto_20190831_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetnumber', models.CharField(max_length=100)),
                ('assettype', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, choices=[('Instock', 'Instock'), ('Allocated', 'Allocated'), ('Scarp', 'Scarp')], max_length=20, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Department')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(blank=True, choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=20, null=True)),
                ('assetnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.AssetMaster')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Department')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assetrequest.Location')),
            ],
        ),
    ]
