from django.db import models
from jsonfield import JSONField
# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50 , primary_key=True)
    name = models.CharField(max_length=20)
    phone_no = models.CharField( max_length=12, default="")
    email_id=models.CharField( max_length=50, default="")
    password = models.CharField( max_length=50 , null=False)
    dp = models.CharField( max_length=50 , default="")
    seller=models.BooleanField(null=True)
    def __str__(self):
        return self.id

class Product(models.Model):
    product_id = models.CharField(max_length=50 , primary_key=True)
    product_name = models.CharField(max_length=20)
    product__image = models.CharField( max_length=12, default="")
    product_description_=models.CharField( max_length=150, default="")
    mrp = models.CharField( max_length=50 , null=False)
    discount = models.CharField( max_length=50 , default="")
    current_price = models.CharField( max_length=50 , default="")
    seller_id = models.CharField( max_length=50 , default="")
    company_name = models.CharField( max_length=50 , default="")
    product__image1 = models.CharField( max_length=12, default="")
    product__image2 = models.CharField( max_length=12, default="")
    product__image3 = models.CharField( max_length=12, default="")
    def __str__(self):
        return self.product_id