# Generated by Django 3.2.6 on 2022-04-28 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220428_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexchange',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.exchange', unique=True),
        ),
    ]