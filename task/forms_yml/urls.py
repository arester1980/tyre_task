from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('tyre/', views.tyre_new, name='tyre_new'),
    path('list/worker', views.tyre_new, name='tyre_new'),
]
