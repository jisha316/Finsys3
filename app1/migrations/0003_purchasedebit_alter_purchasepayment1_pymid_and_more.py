# Generated by Django 4.0.4 on 2022-10-26 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_purchasepayment1_duedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasedebit',
            fields=[
                ('pdebitid', models.AutoField(primary_key=True, serialize=False, verbose_name='pdid')),
                ('debit_no', models.IntegerField(default=1000)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('debitdate', models.DateField(null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('taxamount', models.CharField(max_length=100, null=True)),
                ('grandtotal', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='purchasepayment1',
            name='pymid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='py1id'),
        ),
        migrations.CreateModel(
            name='purchasedebit1',
            fields=[
                ('pdebid', models.AutoField(primary_key=True, serialize=False, verbose_name='pddid')),
                ('items', models.CharField(max_length=100, null=True)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('pdebit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
            ],
        ),
    ]
