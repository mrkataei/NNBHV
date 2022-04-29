# Generated by Django 3.2.6 on 2022-04-28 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_alter_userexchange_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.CharField(max_length=15)),
                ('coin', models.CharField(max_length=15)),
                ('timeframe', models.CharField(max_length=15)),
                ('position', models.CharField(choices=[('S', 'Sell'), ('B', 'Buy')], max_length=1)),
                ('price', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.CharField(max_length=15)),
                ('coin', models.CharField(max_length=15)),
                ('timeframe', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('position', models.CharField(choices=[('S', 'Sell'), ('B', 'Buy')], max_length=1)),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('signal_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStrategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_percent', models.FloatField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.coin')),
                ('exchange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.exchange')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.strategies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
