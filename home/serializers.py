from rest_framework import serializers
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','email')

class IMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model=IMDB
        field=['title','year','rating','genre']
        # explicit= '__all__'
        exclude=[]
        # field='__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        
        

