# Generated by Django 4.1.6 on 2023-02-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_alter_company_cards_alter_company_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cards',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='company',
            name='users',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
