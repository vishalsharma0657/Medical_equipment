# Generated by Django 3.2.9 on 2022-09-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone_no', models.CharField(default='', max_length=12)),
                ('email_id', models.CharField(default='', max_length=12)),
            ],
        ),
    ]
