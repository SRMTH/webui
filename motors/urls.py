from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("qr/<int:id>", views.qrcode, name="qrcode"),
]
