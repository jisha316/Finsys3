# Generated by Django 4.0.4 on 2022-10-29 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_bill_item_purchasebill_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='porder_item',
            new_name='purchaseorder_item',
        ),
    ]
