# Generated by Django 3.1.7 on 2021-05-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BhavcopyRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_code', models.TextField()),
                ('sc_name', models.TextField()),
                ('sc_open', models.FloatField()),
                ('sc_high', models.FloatField()),
                ('sc_low', models.FloatField()),
                ('sc_close', models.FloatField()),
            ],
        ),
    ]
