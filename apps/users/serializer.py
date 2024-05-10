from rest_framework import serializers
from .models import User
from ..role.models import Role
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'name','username','email', 'password','phone_no','role_id','created_date','updated_date')
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'name','username','email', 'password','phone_no','role')
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role_name','created_date','updated_date' ]
class LoginSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['email', 'password']

 
 