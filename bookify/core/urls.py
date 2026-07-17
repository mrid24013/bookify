from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/login/', auth_views.obtain_auth_token),
]
