from .models import EMP
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EMPSerializer, LoginSerializer

class SignupAPIView(GenericAPIView):
    queryset = EMP.objects.all()
    serializer_class = EMPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Signup successful"}, status=201)
        return Response(serializer.errors, status=400)
    
class LoginAPIView(GenericAPIView):
    queryset = EMP.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email or not password:
            return Response({"error": "Please provide both email and password."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = EMP.objects.get(email=email)
        except EMP.DoesNotExist:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        if user.password != password:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(user)
        return Response("you are successfuly logged in", status=status.HTTP_200_OK)   