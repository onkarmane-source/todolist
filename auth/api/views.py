from django.contrib.auth import logout, login
from django.contrib.auth import authenticate, get_user_model
# rest_framework
from rest_framework import permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# relative imports
from .serializers import UserSerializer
from .permissions import AnonPermissionOnly
User = get_user_model()


class AuthView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"data": "You are already authenticated"})
        data = request.data
        uname = data.get("username")
        password = data.get("password")
        qs = User.objects.filter(username=uname).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                login(request, user)
                return Response({"Message": "Successfully Logged in"}, status=200)
        return Response({"data": "Invalid Credentials"}, status=401).add_post_render_callback


# Register ENDPOINT Handler
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout ENDPOINT Handler


class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"Message": "Successfully Logged out"}, status=200)
