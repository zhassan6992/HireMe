from rest_framework import serializers
from client.models import Client
from hero.models import Hero
from .models import Job ,HiringRequest,AcceptedRequest

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','name','phone_number','address','city','governament','date_of_birth')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','title')

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name','phone_number','address','city','governament','date_of_birth','job')

class HiringSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiringRequest
        fields = ('id','client_id','hero_id')

class AcceptedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedRequest
        fields = ('id','client_id','hero_id')
