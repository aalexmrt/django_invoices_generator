# Generated by Django 4.1.5 on 2023-02-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0016_rename_tax_base_invoice_total_base_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
