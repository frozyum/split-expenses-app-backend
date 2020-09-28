import jwt
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from authentication.serializers import UserSerializer, LoginSerializer
from django.contrib import auth
from split_expenses_app_backend import settings


# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username', '')
            password = request.data.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
                data = {'user': serializer.data, 'token': auth_token}
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'Message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
