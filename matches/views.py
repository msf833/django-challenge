from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MatchSerializer
from .models import Match
from rest_framework import viewsets
from rest_framework import generics, permissions
 
# Create your views here.


class MatchView(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()



    