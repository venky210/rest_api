from django.contrib import admin

# Register your models here.
from api_app.models import *


admin.site.register(CustomUser)


admin.site.register(Product)


admin.site.register(Wishlist)


admin.site.register(Cart)

admin.site.register(Category)

admin.site.register(Rating)

admin.site.register(Coupon)