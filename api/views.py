from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework .response import Response
from .seriallizers import TodoSerializer
from todo.models import Todo
from .permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TodoList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user)
            
    serializer_class = TodoSerializer



    