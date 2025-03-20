from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import CustomTokenObtainPairView, RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserView.as_view(), name='me'),  # Ver datos del usuario autenticado
]