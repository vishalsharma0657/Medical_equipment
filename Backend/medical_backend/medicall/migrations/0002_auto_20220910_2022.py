# Generated by Django 3.2.9 on 2022-09-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='seller',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]