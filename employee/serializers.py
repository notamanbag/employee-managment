from rest_framework import serializers




class CreateEmployeeSerliazer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

class EmployeeLoginSerliazer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
class UpdateEmployeeSerliazer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=100,required=False)
    fname = serializers.CharField(max_length=100,required=False)
    lname = serializers.CharField(max_length=100,required=False)
    role = serializers.IntegerField(required=False,default=1)

class CreateOrUpdateProjectSerliazer(serializers.Serializer):
    project_id = serializers.IntegerField()
    name = serializers.EmailField(max_length=100, required=False)
    description = serializers.CharField(max_length=1000,required=False)
    status = serializers.CharField(max_length=50, required=False)
    leader = serializers.IntegerField(required=False)
    priority = serializers.CharField(max_length=10, required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)

    def validate_start_date(self, value):
        # Add custom validation for start_date if needed
        return value

    def validate_end_date(self, value):
        # Add custom validation for end_date if needed
        return value


