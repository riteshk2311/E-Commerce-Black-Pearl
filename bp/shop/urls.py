from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("checkout/", views.checkout, name="Checkout"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
]
