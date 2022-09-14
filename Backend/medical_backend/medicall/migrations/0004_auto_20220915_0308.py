# Generated by Django 3.2.9 on 2022-09-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicall', '0003_alter_user_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('product_image', models.CharField(default='', max_length=12)),
                ('product_description', models.CharField(default='', max_length=150)),
                ('mrp', models.CharField(max_length=50)),
                ('discount', models.CharField(default='', max_length=50)),
                ('current_price', models.CharField(default='', max_length=50)),
                ('seller_id', models.CharField(default='', max_length=50)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('product_image1', models.CharField(default='', max_length=12)),
                ('product_image2', models.CharField(default='', max_length=12)),
                ('product_image3', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
