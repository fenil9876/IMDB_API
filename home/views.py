from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
from .models import IMDB
from rest_framework.views import APIView
from rest_framework import generics

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=()
    
class IMDB_API(APIView):
    
    def get(self,request):
        movie_objs=IMDB.objects.all()
        serializer=IMDBSerializer(movie_objs,many=True)
        return Response({'status':2000,"payload": serializer.data})
    
    def post(self,request):
        data=request.data
        serializer=IMDBSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({'status':403,"eroor": serializer.errors,"message": "something went wrong"})
        serializer.save()
        print(data)
        return Response({'status':2000,"payload": serializer.data,"message":"you data is saved"})
    
    def patch(self,request):
        try:
            movie_objs=IMDB.objects.get(id=request.data['id'])
            serializer=IMDBSerializer(movie_objs,data=request.data,partial=True)
            
            if not serializer.is_valid():
                return Response({'status':403,"eroor": serializer.errors,"message": "something went wrong"})
            serializer.save()
            # print(data)
            return Response({'status':2000,"payload": serializer.data,"message":"you data is updated"})
        
        except Exception as e:
            return Response({"status":403,'message':'invalid id'})
    
    def put(self,request):
        pass
    
    def delete(self,request):
        try:
            movie_objs=IMDB.objects.get(id=request.GET.get('id'))
            movie_objs.delete()
            return Response({'status':2000,"message":"deleted"})
        
        except Exception as e:
            return Response({"status":403,'message':'invalid id'})
    

class Review(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@api_view(['POST'])
def createReview(self,request):
    data=request.data
    serializer=ReviewSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,"eroor": serializer.errors,"message": "something went wrong"})
    print(data)
    serializer.save()
    return Response({'status':2000,"payload": serializer.data,"message":"you data is saved"})













