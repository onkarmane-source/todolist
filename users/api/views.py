from django.contrib.auth import logout,login
from django.contrib.auth import authenticate, get_user_model

# rest_framework
from rest_framework import permissions, generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

# relative imports
from .serializers import UserSerializer, LoginSerializers
from .permissions import AnonPermissionOnly

User=get_user_model()


# Login ENDPOINT Handler
# class AuthView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializers(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         # update_last_login(None, user)
#         # token, created = Token.objects.get_or_create(user=user)
#         return Response({"status": status.HTTP_200_OK})




class AuthView(APIView):
    # serializer_class    =  LoginSerializers
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"data":"You are already authenticated"})
        data=request.data
        uname=data.get("username")
        password=data.get("password")
        qs=User.objects.filter(username=uname).distinct()
        if qs.count()==1:
            user_obj=qs.first()
            if  user_obj.check_password(password):
                user=user_obj
                login(request,user)
                return Response({"Message":"Successfully Logged in"},status=200)
        return Response({"data":"Invalid Credentials"},status=401).add_post_render_callback

# Register ENDPOINT Handler 
class RegisterAPIView(generics.CreateAPIView):
    queryset            =  User.objects.all()
    serializer_class    =  UserSerializer
    permission_classes  =  [AnonPermissionOnly]

    def get_serializer_context(self, *args,**kwargs):
        return {"request": self.request}

# Logout ENDPOINT Handler
class LogoutAPIView(APIView):
    def post(self,request,*args,**kwargs):
        logout(request)
        return Response({"Message":"Successfully Logged out"},status=200)