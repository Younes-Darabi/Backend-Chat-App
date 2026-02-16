from django.contrib import admin
from django.urls import path
from chat_app import views

urlpatterns = [
    path('', views.Chat_View.as_view()),
]