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
    
class UpdateEmployee(views.APIView):
    
    serializer_class = serializers.UpdateEmployeeSerliazer
    @csrf_exempt
    def post(self,request):
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            user_id = serialized_data.validated_data.get('user_id')
            # Assuming 'user_id' is a valid identifier for the employee you want to update

            try:
                # Fetch the employee from the database
                employee = models.User.objects.get(id=user_id)

                # Update employee details based on the provided data
                employee.fname = serialized_data.validated_data.get('first_name', employee.fname)
                employee.lname = serialized_data.validated_data.get('last_name', employee.lname)
                employee.role = serialized_data.validated_data.get('role', employee.role)
                employee.password = serialized_data.validated_data.get('password', employee.password)
                


                # Save the updated employee
                employee.save()

                return Response({'message': 'Employee updated successfully'}, status=status.HTTP_200_OK)
            
            except models.User.DoesNotExist:
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
            
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class EmployeeLogin (views.APIView):
    
    serializer_class = serializers.EmployeeLoginSerliazer
    def post(self,request):
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            # Assuming 'user_id' is a valid identifier for the employee you want to update

            try:
                # Fetch the employee from the database
                email = serialized_data.get('email',None)
                password = serialized_data.get('password',None)
                
                current_user = models.User.objects.filter(user=email)
                if current_user and current_user.password == password:
                    return Response({'message': 'Logged In'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Please recheck your email or password'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:   
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateOrUpdateProject(views.APIView):
    
    serializer_class = serializers.CreateOrUpdateProjectSerliazer
    
    @csrf_exempt
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            project_id = serialized_data.validated_data.get('project_id')

            try:
                if project_id:
                    project = models.Projects.objects.get(id=project_id)
                else:
                    project = models.Projects.objects.create()


                # Update project details based on the provided data
                project.name = serialized_data.validated_data.get('name', project.name)
                project.description = serialized_data.validated_data.get('description', project.description)
                project.status = serialized_data.validated_data.get('status', project.status)
                project.leader = serialized_data.validated_data.get('leader', project.leader)
                project.priority = serialized_data.validated_data.get('priority', project.priority)
                project.start_date = serialized_data.validated_data.get('start_date', project.start_date)
                project.end_date = serialized_data.validated_data.get('end_date', project.end_date)

                # Save the updated project
                project.save()

                return Response({'message': 'Project updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    

    
        
    
