from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
# Create your views here.
from . import models
from django.http import HttpResponse
from . import serializers
import uuid

class CreateEmployee(views.APIView):
    
    
    serializer_class = serializers.CreateEmployeeSerliazer
    def generate_new_email(self,fname, lname):
        # Combine first and last names
        full_name = fname.lower() + lname.lower()

        # Ensure minimum length of 8 characters
        if len(full_name) < 8:
            email_id = full_name + "123"  # Appending '123' to meet minimum length
        else:
            email_id = full_name

        # Adding a unique identifier using uuid
        unique_id = str(uuid.uuid4().hex)[:8]  # Extracting the first 8 characters of the UUID

        # Adding a common email domain (you can customize this)
        email = email_id + unique_id + "@example.com"

        return email
        
    @csrf_exempt
    def post(self,request):
        serliazed_data = self.serializer_class(data=request.data)
        first_name=None
        last_name=None
        if serliazed_data.is_valid():
            first_name=serliazed_data.validated_data.get('first_name')
            last_name=serliazed_data.validated_data.get('last_name')
        
        if first_name and last_name:
            generated_email = self.generate_new_email(first_name,last_name)
        
        try:
            new_user_entry = models.User.objects.create(fname=first_name,lname = last_name,email = generated_email,role=1)
            response_data = {'email': generated_email}
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error': 'Error creating user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
    
