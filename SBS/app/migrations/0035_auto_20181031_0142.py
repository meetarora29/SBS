# Generated by Django 2.1.1 on 2018-10-30 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20181031_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('read_user', 'Read User'), ('edit_user', 'Edit User'))},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'permissions': (('read_transaction', 'Read Transaction'), ('edit_transaction', 'Edit Transaction'))},
        ),
    ]
