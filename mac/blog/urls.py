
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogPost"),
    # path("contact/", views.contact, name="ContactUS"),
    # path("tracker/", views.tracker, name="TrackingStatus"),
    # path("search/", views.search, name="Search"),
    # path("productview/", views.productView, name="Search"),
    # path("checkout/", views.checkout, name="checkout"),
]

