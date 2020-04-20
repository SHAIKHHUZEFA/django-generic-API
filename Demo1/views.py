from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Demo
from .serializers import BookSerializer
from rest_framework import generics
from .import serializers

# Create your views here.

def homepage(request):
    return render(request,"/Users/Huzefa/PycharmProjects/genericAPIpro/Testing/Demo1/templates/home.html")

class AddBook(generics.CreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = serializers.BookSerializer

class retrieveAdddbook(generics.ListCreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = serializers.BookSerializer

class viewAllBook(generics.ListAPIView):
    queryset = Demo.objects.all()
    serializer_class = serializers.BookSerializer

class UpdateBook(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Demo.objects.all()
    serializer_class = serializers.BookSerializer

class DeleteBook(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Demo.objects.all()
    serializer_class = serializers.BookSerializer


