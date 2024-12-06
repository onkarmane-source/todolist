from rest_framework import generics, permissions
from .serializers import *
from mainapp.models import ToDoList
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# list all tasks


class ListToDo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

# PUT


class Detailview(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     request.data.update({'voucherrows': json.loads(request.data.pop('voucherrows', None))})
    #     return super().update(request, *args, **kwargs)

# Create Task


class Createview(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


# class Deleteview(generics.DestroyAPIView):
#     queryset = ToDoList.objects.all()
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     serializer_class = TaskSerializer

# # class Deleteview(generics.DestroyAPIView):
# #     queryset = ToDoList.objects.all()
# #     serializer_class = TaskSerializer

# #     def destroy(self, request, *args, **kwargs):
# #         instance = self.get_object()
# #         # Serialize the object to be deleted
# #         serializer = self.get_serializer(instance)
# #         self.perform_destroy(instance)
# #         return Response({
# #             'message': 'The following ToDo item has been deleted:',
# #             'deleted_todo': serializer.data
# #         }, status=status.HTTP_200_OK)

class Deleteview(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TaskSerializer

    def preview(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'message': 'Preview of todo',
            'todo_item': serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response({
            'message': 'Todo deleted successfully:',
            'deleted_todo': serializer.data
        }, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.preview(request, *args, **kwargs)


class Updateview(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
