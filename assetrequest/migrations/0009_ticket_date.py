# Generated by Django 2.2.4 on 2019-08-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequest', '0008_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]