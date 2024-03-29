# Generated by Django 3.2.6 on 2022-04-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('coin', models.CharField(max_length=10)),
                ('timeframe', models.CharField(max_length=4)),
                ('total_tades', models.IntegerField(default=0)),
                ('net_profit', models.FloatField()),
                ('accuracy', models.FloatField()),
                ('positive_trades', models.FloatField()),
                ('average_trade_profit', models.FloatField()),
                ('profit_per_coin', models.FloatField()),
                ('final_amount', models.FloatField()),
            ],
        ),
    ]
