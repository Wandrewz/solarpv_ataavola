# Generated by Django 3.0.5 on 2020-04-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]