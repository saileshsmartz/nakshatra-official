from django.urls import path

from . import views
from .api import apiViews

urlpatterns=[
    path("product/new/", apiViews.new, name="newProduct"),
    path("products/<int:id>", apiViews.delete, name="deleteProduct"),
    path("products/edit/<int:id>/", apiViews.edit, name="editProduct"),
    path("products/", apiViews.all, name="showAll"),
    path("api/product/<int:id>", apiViews.productsApi.as_view(), name="productDetails"),
]

urlpatterns += [
    path("index", views.index),
    path("contact",views.contact),
    path("login",views.login),
    path("work/<int:id>",views.work)
] 
