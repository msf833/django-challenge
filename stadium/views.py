from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StadiumSerializer
from .models import Stadium
from rest_framework import viewsets
 
# Create your views here.


class StadiumView(viewsets.ModelViewSet):
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()



    