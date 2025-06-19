from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the Django internship project!")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User

class PublicEndpoint(APIView):
    permission_classes = []  # No authentication required
    def get(self, request):
        return Response({"message": "This is a public endpoint accessible to everyone."})

class ProtectedEndpoint(APIView):
    permission_classes = [IsAuthenticated]  # Requires authentication
    def get(self, request):
        messages = Message.objects.filter(owner=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserRegister(APIView):
    permission_classes = []  # Public endpoint for registration
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully"}, status=201)
        return Response({"error": "Invalid data"}, status=400)