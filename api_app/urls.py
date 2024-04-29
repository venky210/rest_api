from django.urls import path
from api_app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Registration/',Registration,name='Registration'),
    path('login/',login,name='login'),
    path('ChangePassword/',ChangePassword,name='ChangePassword'),
  
    path('editprofile/',editprofile,name='editprofile'),
    path('CreateProduct/',CreateProduct,name='CreateProduct'),
    path('dealer_product_list/',dealer_product_list,name='dealer_product_list'),
    path('allproducts/',allproducts,name='allproducts'),
    path('updateproduct/<int:product_id>/',updateproduct,name='updateproduct'),
    path('productdelete/<int:product_id>/',productdelete,name='productdelete'),

    path('addwishlist/<int:product_id>/',addwishlist,name='addwishlist'),
    path('wishlist/',wishlist,name='wishlist'),
    path('removewishlist/<int:product_id>/',removewishlist,name='removewishlist'),

    path('addtocart/<int:product_id>/',addtocart,name='addtocart'),
    path('cartlist/',cartlist,name='cartlist'),
    path('removecart/<int:product_id>/',removecart,name='removecart'),

    path('createcategory/',createcategory,name='createcategory'),
    path('categorylist/',categorylist,name='categorylist'),
    path('deletecategory/<int:category_id>/',deletecategory,name='deletecategory'),
    path('updatecategory/<int:category_id>/',updatecategory,name='updatecategory'),
    path('categorydetails/<int:category_id>/',categorydetails,name='categorydetails'),

    path('lowtohigh/',lowtohigh,name='lowtohigh'),
    path('hightolow/',hightolow,name='hightolow'),

    path('updatestatus/<int:product_id>/',updatestatus,name='updatestatus'),

    path('import_from_excel/',import_from_excel,name='import_from_excel'),

    path('rating/<int:product_id>/',rating,name='rating'),
    path('ratinglist/',ratinglist,name='ratinglist'),
    
    path('createcoupon/',createcoupon,name='createcoupon'),
    path('coupon_list/',coupon_list,name='coupon_list'),
    path('coupon_detail/<int:pk>/',coupon_detail,name='coupon_detail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
