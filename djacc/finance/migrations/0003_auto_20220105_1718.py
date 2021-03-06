# Generated by Django 3.2.10 on 2022-01-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_customer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('t_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditor', to='finance.customer')),
                ('t_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitor', to='finance.customer')),
            ],
        ),
    ]
