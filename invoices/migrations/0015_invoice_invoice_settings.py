# Generated by Django 4.1.5 on 2023-02-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_alter_client_zip_code_alter_company_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoicesetting'),
        ),
    ]