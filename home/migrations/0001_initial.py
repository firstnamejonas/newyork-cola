# Generated by Django 3.2.25 on 2024-05-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_first_name', models.CharField(max_length=100)),
                ('newsletter_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
