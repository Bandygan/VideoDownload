from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path
from .views import LinkListCreateView, LinkDestroyView, index, generate_telegram_setup_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/links/', LinkListCreateView.as_view(), name='link-list-create'),
    path('api/v1/links/<int:pk>/', LinkDestroyView.as_view(), name='link-destroy'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout', LogoutView.as_view()),
    path('telecode', generate_telegram_setup_code, name='generate_telegram_setup_code'),
    path(r"", index, name='profile'),
    path(r"user", index, name='profile'),

    # re_path(r"^.*$", index, name='index'),
]


