import imp
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('new/',views.new,name="new"),
    path('show/<str:id>/',views.show,name="show"),
    path('delete/<str:id>/',views.delete,name="delete"),
    path('<str:id>/edit/',views.edit,name="edit"),
]