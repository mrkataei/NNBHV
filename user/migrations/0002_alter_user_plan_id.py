# Generated by Django 3.2.6 on 2022-04-28 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='plan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.plan'),
        ),
    ]