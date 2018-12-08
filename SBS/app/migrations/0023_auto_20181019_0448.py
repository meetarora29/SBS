# Generated by Django 2.1.1 on 2018-10-18 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181019_0417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': (('read_account', 'Read Account'),)},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('read_user', 'Read User'),)},
        ),
        migrations.AlterModelOptions(
            name='pii',
            options={'permissions': (('read_pii', 'Read PII'),)},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'permissions': (('read_transaction', 'Read Transaction'),)},
        ),
    ]
