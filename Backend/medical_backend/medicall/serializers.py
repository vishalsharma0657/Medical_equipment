from pickle import FALSE
from rest_framework import serializers
from medicall.models import User
from medicall.models import Product

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50 )
    name = serializers.CharField(max_length=20)
    phone_no = serializers.CharField( max_length=12 , default="")
    email_id = serializers.CharField( max_length=50 , default="")
    password = serializers.CharField( max_length=50 , default="")
    dp = serializers.CharField( max_length=50 , allow_null=False)
    seller=serializers.NullBooleanField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.password = validated_data.get('password', instance.password)
        instance.dp = validated_data.get('dp', instance.dp)
        instance.seller=validated_data.get('seller',instance.seller)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=50 )
    product_name = serializers.CharField(max_length=20)
    product__image = serializers.CharField( max_length=12 , default="")
    product_description = serializers.CharField( max_length=50 , default="")
    mrp = serializers.CharField( max_length=50 , default="")
    discount =  serializers.CharField( max_length=50 , default="")
    current_price = serializers.CharField( max_length=50 , default="")
    seller_id = serializers.CharField( max_length=50 , default="")
    company_name = serializers.CharField( max_length=50 , default="")
    product_image1 = serializers.CharField( max_length=12, default="")
    product_image2 = serializers.CharField( max_length=12, default="")
    product_image3 = serializers.CharField( max_length=12, default="")


    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('id', instance.product_id)
        instance.product_name = validated_data.get('name', instance.product_name)
        instance.product__image = validated_data.get('phone_no', instance.product__image)
        instance.product_description = validated_data.get('email_id', instance.product_description)
        instance.mrp = validated_data.get('password', instance.mrp)
        instance.discount = validated_data.get('dp', instance.discount)
        instance.seller_id = validated_data.get('seller',instance.seller_id)
        instance.company_name = validated_data.get('seller',instance.company_name)
        instance.product_image1 = validated_data.get('seller',instance.product_image1)
        instance.product_image2 = validated_data.get('seller',instance.product_image2)
        instance.product_image3 = validated_data.get('seller',instance.product_image3)
        instance.save()
        return instance
