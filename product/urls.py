
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('newproducts/',views.newproducts,name="newproducts"),
    path('cart/',views.cart1,name="cart1"),
    path('add/<int:proid>',views.add,name="add"),
    path('delete/<int:proid>',views.delet,name="delet"),
]
