from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('file/<id>', views.FileView.as_view(), name='file')
]
