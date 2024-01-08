from rest_framework import serializers




class CreateEmployeeSerliazer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)