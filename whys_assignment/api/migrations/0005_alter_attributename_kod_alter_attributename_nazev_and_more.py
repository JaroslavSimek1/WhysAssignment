# Generated by Django 4.0.6 on 2022-07-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_attributename_nazev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributename',
            name='kod',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attributename',
            name='nazev',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attributename',
            name='zobrazit',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
