from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('list/', views.list_tyre, name='list'),
    path('result/', views.upload_file, name='result'),
    path('save/', views.save, name='save'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
