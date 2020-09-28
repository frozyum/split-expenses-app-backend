from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from authentication.serializers import UserSerializer

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)