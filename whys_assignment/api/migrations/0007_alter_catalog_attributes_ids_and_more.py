# Generated by Django 4.0.6 on 2022-07-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_attributevalue_hodnota_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='attributes_ids',
            field=models.ManyToManyField(blank=True, to='api.attribute'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='products_ids',
            field=models.ManyToManyField(blank=True, to='api.product'),
        ),
    ]
