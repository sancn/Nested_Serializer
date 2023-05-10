from django.shortcuts import render
from .serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets
from .models import *

# Create your views here.
class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

    def get_serializer_context(self):
       context=super().get_serializer_context()
       context['request']= self.request
       return context
      #  return {"request": self.request}

class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer