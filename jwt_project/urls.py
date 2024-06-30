from django.contrib import admin
from django.urls import path, include
from .views import LinkListCreateView, LinkDestroyView, index
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/links/', LinkListCreateView.as_view(), name='link-list-create'),
    path('api/v1/links/<int:pk>/', LinkDestroyView.as_view(), name='link-destroy'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', index, name='index'),
]
