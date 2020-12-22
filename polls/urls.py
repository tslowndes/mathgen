from django.urls import path

from . import views

urlpatterns = [
    path('qs/', views.index, name='index'),
    path('sub/', views.subcontents, name='subcontents'),
    path('', views.contents, name='contents')
]
