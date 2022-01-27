from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework import viewsets
from rest_framework import generics, permissions
 
# Create your views here.


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()



    