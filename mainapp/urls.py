from django.contrib import admin
from django.urls import path, include
from .views import home_view
# from .views import AuthView,RegisterAPIView,LogoutAPIView

urlpatterns = [
    # path('login/', AuthView.as_view()),
    # path('register/', RegisterAPIView.as_view()),
    # path('logout/', LogoutAPIView.as_view()),
    path("api/main/", include("mainapp.api.urls")),
    path("", home_view),
    path('api/auth/', include('auth.api.urls'))
]
