from django.shortcuts import render
from pageapp.models import Employee
from pageapp.serializers import EmployeeSerializer
from rest_framework import generics
from pageapp.pagination import MyPaginatiion
class EmployeeAPIView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPaginatiion
    search_fields=('ename','eno')
    ordering_fields=('eno','esal')

# Create your views here.
