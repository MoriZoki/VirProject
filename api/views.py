from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
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
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
            
    serializer_class = TodoSerializer
    filterset_fields = ["title", "status", "category", "user__username", "end_time"]
    search_fields = ["title", "description", "status"]
    ordering_fields = ["end_time", "status", "category"]


# for retrieve update and delete all in one endpoint 

class TodoEdit(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

# just for update a todo in one endpint 
class TodoUpdate(UpdateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

# just for destroy (delete) a object in one endpint 
class TodoDestroy(DestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user)
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer



    