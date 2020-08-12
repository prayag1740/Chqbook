# Generated by Django 3.1 on 2020-08-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razorpay', '0003_auto_20200812_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Created'), (1, 'Attempted'), (2, 'Paid')], null=True),
        ),
    ]