from django.urls import path

from . import views

app_name = "store"

urlpatterns =[
    path("", views.Homepage , name = "index"),
    path("cart/", views.cart, name = "cart")
]