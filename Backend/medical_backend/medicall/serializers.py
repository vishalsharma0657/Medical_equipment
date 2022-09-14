from pickle import FALSE
from rest_framework import serializers
from medicall.models import User

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
        