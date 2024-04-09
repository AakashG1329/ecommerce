from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import Role, User
from users.serializer import RoleSerializer, UserCreateSerializer, UserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.models import Token
from django.contrib.auth import models

class login(APIView):
    def post(self,request):
        user=get_object_or_404(User,username=request.data.get('username'))
        print(user.password)
        if  user.password !=request.data['password']:
            return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user.status)
        # serializer = UserSerializer(queryset, many=True)
        return Response({"token": token.key, "user": user})





class userLogin(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')
                print(serializer)
                if not User.objects.filter(email=email).exists():

                    msg = {"code": status.HTTP_400_BAD_REQUEST, 'msg': 'Invalid Credentials'}
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                
                # user = authenticate(email=email, password=password)
                # if user is not None:

                #     refresh = RefreshToken.for_user(user)
                #     return JsonResponse({
                #           'access_token': str(refresh.access_token),
                #           'refresh_token': str(refresh)
                #                  })
                else:
                    print(email)
                    token = RefreshToken.for_user(email).access_token
                    # user = authenticate(request, email=email, password=password)
                    # refresh = RefreshToken.for_user(user)
                    return JsonResponse({
                          'access_token': str(token),
                          'refresh_token': str(token)
                                 })
        # user = authenticate(request, email=email, password=password)

        



class userGet(APIView):
    permission_classes = (IsAuthenticated) 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,id):
        try:  
        # Filter queryset based on 'id'
            queryset = User.objects.filter(id=id)
            # queryset = self.get_queryset()
            serializer = UserSerializer(queryset, many=True)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
class userGetAll(APIView):
    def get_queryset(self):
        return User.objects.all().order_by('id')
    def get(self,request):
        try:
            queryset = self.get_queryset() 
            serializer = UserSerializer(queryset, many=True)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        
class userPost(APIView):
        serializer_class = UserCreateSerializer
        queryset = User.objects.all()
        def post(self, request):
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                username = serializer.validated_data.get('username')
                if User.objects.filter(email=email).exists():
                    msg = {"code": status.HTTP_400_BAD_REQUEST, 'msg': 'Email id Already Exists'}
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                if User.objects.filter(username=username).exists():
                    msg = {"code": status.HTTP_400_BAD_REQUEST, 'msg': 'Username Already Exists'}
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                msg = {"code": status.HTTP_201_CREATED, 'msg': 'User_Data Created Successfully',
                       'data': serializer.data}
                return Response(msg, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class userUpdate(APIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def put(self,request):
        try:
            id = request.data.get('id')
            obj = User.objects.get(id=id)
            obj1 = UserSerializer(obj, data=request.data)
            
            if obj1.is_valid():
                obj1.save()
                print(obj1.data)
                msg = {"code": status.HTTP_201_CREATED, "msg": "Data Updated Successfully", "data": obj1.data}
                return Response(msg,status=status.HTTP_205_RESET_CONTENT)
        except User.DoesNotExist:
            msg = {"code": status.HTTP_404_NOT_FOUND, "msg": "Invalid ID"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
class userDelete(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,id):
        try:  
        # Filter queryset based on 'id'
            queryset = User.objects.filter(id=id)
            queryset.delete()
            msg = {'code': status.HTTP_204_NO_CONTENT, 'msg': 'Datas Get Successfully'}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    

# role
class roleGet(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    def get(self,request,id):
        try:  
        # Filter queryset based on 'id'
            queryset = Role.objects.filter(id=id)
            # queryset = self.get_queryset()
            serializer = RoleSerializer(queryset, many=True)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
class roleGetAll(APIView):
    def get_queryset(self):
        return Role.objects.all().order_by('id')
    def get(self,request):
        try:
            queryset = self.get_queryset() 
            serializer = RoleSerializer(queryset, many=True)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        
class rolePost(APIView):
        serializer_class = RoleSerializer
        queryset = Role.objects.all()
        def post(self, request):
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {"code": status.HTTP_201_CREATED, 'msg': 'Role_Data Created Successfully',
                       'data': serializer.data}
                return Response(msg, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class roleUpdate(APIView):
    
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    def put(self,request):
        try:
            id = request.data.get('id')
            obj = Role.objects.get(id=id)
            obj1 = RoleSerializer(obj, data=request.data)
            
            if obj1.is_valid():
                obj1.save()
                print(obj1.data)
                msg = {"code": status.HTTP_201_CREATED, "msg": "Data Updated Successfully", "data": obj1.data}
                return Response(msg,status=status.HTTP_205_RESET_CONTENT)
        except Role.DoesNotExist:
            msg = {"code": status.HTTP_404_NOT_FOUND, "msg": "Invalid ID"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
class roleDelete(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    def get(self,request,id):
        try:  
        # Filter queryset based on 'id'
            queryset = Role.objects.filter(id=id)
            queryset.delete()
            msg = {'code': status.HTTP_204_NO_CONTENT, 'msg': 'Datas Get Successfully'}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except Role.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    