# Generated by Django 4.2.6 on 2024-02-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_studentquiz_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
