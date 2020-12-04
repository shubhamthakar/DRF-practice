from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list, name="article"),
    path('details/<int:pk>/', views.article_detail, name="details")
]