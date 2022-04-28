# Generated by Django 3.2.6 on 2022-04-28 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userstrategies',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.coin'),
        ),
    ]