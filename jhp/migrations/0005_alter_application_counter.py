# Generated by Django 4.1.1 on 2022-09-05 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhp', '0004_application_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='counter',
            field=models.PositiveIntegerField(default=1),
        ),
    ]