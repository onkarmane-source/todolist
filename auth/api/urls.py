from django.urls import path
from .views import AuthView,RegisterAPIView,LogoutAPIView

urlpatterns = [ 
    path('login/', AuthView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]