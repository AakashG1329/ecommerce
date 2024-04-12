from rest_framework import serializers
from .models import User
from ..role.models import Role
class UserSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='User.name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name','username','email', 'password','phone_no','role_id','created_date','updated_date')
        extra_kwargs = {
            'password':{'write_only': True},
        }

class UserCreateSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='User.name', read_only=True)

    class Meta:
        model = User
        fields = "__all__"
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role_name','created_date','updated_date' ]
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

 
 