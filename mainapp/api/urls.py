from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt
from .views import ListToDo, Createview, Detailview, Deleteview, Updateview

urlpatterns = [
    path("<int:pk>/", Detailview.as_view(), name='detail-todo'),
    path("", ListToDo.as_view(), name='list-todos'),
    path("create/", Createview.as_view(), name='create-todo'),
    path("delete/<int:pk>/", Deleteview.as_view(), name='delete-todo'),
    path("update/<int:pk>/", Updateview.as_view(), name='update-todo'),
]
