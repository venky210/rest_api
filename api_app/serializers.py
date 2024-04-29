from api_app.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email','user','dealer']
        extra_kwargs={
           
            'email':{'required':True},
            'user':{'required':True},
            'dealer':{'required':True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegisterSerializers, self).create(validated_data)



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)





class editprofileserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['username', 'email','Address']
        extra_kwargs={
            "email":{"required":True},
            "Address":{"required":True}
        }




class createproductserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','pname','img','qty','price','status','category','productvariation','disscount_per']
        # category=serializers.CharField(source='category.category',read_only=True)
        ratting=serializers.IntegerField(source='product.product',read_only=True)
       

        extra_kwargs={
            "qty":{"required":True},
            "productvariation":{"required":True}, 
            "category":{"required":True}, 
            "img":{"read_only":True}
            
            # "category":{"write_only":True},
            # "category":{"read_only":True}
        }


class productupdateserializer(serializers.ModelSerializer):
    productvariation = serializers.CharField()
    class Meta:
        model=Product
        fields = ['id', 'pname', 'qty', 'price', 'status', 'category', 'productvariation','disscount_per']
       


class wishlistserializer(serializers.ModelSerializer):
    pname=serializers.CharField(source='product.pname',read_only=True)
    img=serializers.ImageField(source='product.img',read_only=True)
    price=serializers.IntegerField(source='product.price',read_only=True)
    productvariation=serializers.CharField(source='product.productvariation',read_only=True)
    disscount_per=serializers.IntegerField(source='product.disscount_per',read_only=True)
    # category=serializers.CharField(source='category.category',read_only=True)
    class Meta:
        model=Wishlist
        # fields='__all__'
        fields=['pname','img','price','qty','productvariation','disscount_per']
        


class Addcartserializer(serializers.ModelSerializer):
    pname=serializers.CharField(source='product.pname',read_only=True)
    img=serializers.ImageField(source='product.img',read_only=True)
    price=serializers.IntegerField(source='product.price',read_only=True)
    productvariation=serializers.CharField(source='product.productvariation',read_only=True)
    disscount_per=serializers.IntegerField(source='product.disscount_per',read_only=True)
  
    class Meta: 
        model=Cart
        # fields='__all__'
        fields=['pname','img','price','quantity','productvariation','disscount_per']



class createcategoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category']



class ratingserializer(serializers.ModelSerializer):
    product=serializers.CharField(source='product.pname',read_only=True)
    class Meta:
        model=Rating
        fields=['product','rating','comment']



class couponserializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'
        extra_kwargs={
            "coupon":{"required":True},
            "user":{"required":True}
        }