from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('tyre/', views.tyre_new, name='tyre_new'),
    path('list/UploadFileForm', views.upload_file, name='tyre_new'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
