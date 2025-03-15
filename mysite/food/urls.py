from tkinter.font import names
from xml.etree.ElementInclude import include

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name="detail"),
]