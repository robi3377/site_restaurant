# Generated by Django 4.0.5 on 2022-07-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mancare',
            name='link_poza',
            field=models.CharField(default='Doamne ajuta', max_length=99),
        ),
        migrations.AddField(
            model_name='mancare',
            name='nume',
            field=models.CharField(default='Doamne ajuta', max_length=50),
        ),
    ]