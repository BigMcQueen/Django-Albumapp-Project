from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PhotoListView, PhotoDetailView, TagPhotoListView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('tag/<str:tag>', TagPhotoListView.as_view(), name='tag_photo_list'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)