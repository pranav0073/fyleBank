# Generated by Django 2.0 on 2019-05-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190521_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='id',
        ),
        migrations.AlterField(
            model_name='branch',
            name='ifsc',
            field=models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]