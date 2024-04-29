from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator

class CustomUser(AbstractUser):
    USER_ROLES=(
        ('user','User'),
        ('dealer','Dealer'),
        ('admin','Admin'),
    )
   

    Address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    mobile_no=models.IntegerField(null=True,blank=True)


    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)

class Category(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.category

class Product(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),)
    
    
    pname=models.CharField(max_length=100)
    qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='product',null=True,blank=True)
    dealer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    productvariation=models.CharField(max_length=100,null=True,blank=True)
    disscount_per=models.IntegerField(blank=True,default=0)
    SKU = models.CharField(max_length=50, blank=True)
    barcode = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.pname
    


class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
  
    qty=models.IntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Cart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)




class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Coupon(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    coupon=models.CharField(max_length=100,unique=True,blank=True,null=True)
    start_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    vaild_date=models.DateTimeField()




