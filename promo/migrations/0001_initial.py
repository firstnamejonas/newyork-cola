# Generated by Django 3.2.25 on 2024-04-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_username', models.CharField(max_length=100)),
                ('contest_ordernumber', models.CharField(max_length=100)),
            ],
        ),
    ]
