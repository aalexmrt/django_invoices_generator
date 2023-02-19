# Generated by Django 4.1.5 on 2023-02-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0012_remove_invoice_tax_base_remove_invoicesetting_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='invoicesetting',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='invoicesetting',
            name='tax_base',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]
