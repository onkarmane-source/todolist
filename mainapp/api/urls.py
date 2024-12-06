from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path("<int:pk>/", Detailview.as_view()),
    path("", ListToDo.as_view()),
    path("create/", Createview.as_view()),
    path("delete/<int:pk>/", Deleteview.as_view()),
    path("update/<int:pk>/", Updateview.as_view()),
]
