from django.urls import path
from .views import AuthView, RegisterAPIView, LogoutAPIView

urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
