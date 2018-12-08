# Generated by Django 2.1.1 on 2018-10-18 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20181019_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='account_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_account', to='app.Account'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='pii_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_pii', to='app.PII'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='transaction_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_transaction', to='app.Transaction'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='user_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_user_obj', to=settings.AUTH_USER_MODEL),
        ),
    ]