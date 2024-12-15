from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Boots
from .serializers import BootsSerializer



class BootsAPIView(APIView):
    def get(self, request):
        w = Boots.objects.all()

        return Response({'posts': BootsSerializer(w, many=True).data})
    
    

    
    def post(self, request):
        serializer = BootsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Boots.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        serializer = BootsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    
    
    
    
    

# class BootsAPIView(generics.ListAPIView):
#     queryset = Boots.objects.all()
#     serializer_class = BootsSerializer