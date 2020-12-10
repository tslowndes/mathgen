from django.urls import path

from . import views

urlpatterns = [
    path('qs/', views.index, name='index'),
    path('', views.subcontents, name='subcontents'),
]
