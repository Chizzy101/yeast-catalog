from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('yeasts/', views.YeastListView.as_view(), name='yeasts'),
    path('yeast/<int:pk>', views.YeastDetailView.as_view(), name='yeast-detail'),
    path('yeast/create/', views.YeastCreate.as_view(), name='yeast-create'),
    path('yeast/<int:pk>/update', views.YeastUpdate.as_view(), name='yeast-update'),
    path('yeast/<int:pk>/delete', views.YeastDelete.as_view(), name='yeast-delete'),
    path('storage/', views.storageList, name='storage'),
    path('storage/<int:pk>', views.StorageInstanceDetailView.as_view(), name='storageinstance-detail'),
    path('storage/create/', views.create_storage_instance, name='storageinstance-create'),
    path('storage/<int:pk>/update', views.update_storage_instance, name='storageinstance-update'),
    path('storage/<int:pk>/delete', views.StorageInstanceDelete.as_view(), name='storageinstance-delete'),
    path('media/', views.MediaListView.as_view(), name='media'),
    path('media/<int:pk>', views.MediaDetailView.as_view(), name='media-detail'),
    path('media/create/', views.MediaCreate.as_view(), name='media-create'),
    path('media/<int:pk>/update', views.MediaUpdate.as_view(), name='media-update'),
    path('media/<int:pk>/delete', views.MediaDelete.as_view(), name='media-delete'),
    path('docs/', views.testdocument, name='test-document'),
]