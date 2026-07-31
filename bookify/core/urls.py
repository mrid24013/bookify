from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/login/', auth_views.obtain_auth_token),
    # Verificacion Postman
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
