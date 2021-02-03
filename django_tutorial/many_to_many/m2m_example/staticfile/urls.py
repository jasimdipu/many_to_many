from django.urls import path
from staticfile import views
urlpatterns = [
    path('', views.index, name='images')
]
