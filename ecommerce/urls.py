"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets
import apps.users
from apps.users import views as userView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userget/<int:id>/',userView.userGet.as_view()),
    path('usergetall/',userView.userGetAll.as_view()),
    path('usercreate/',userView.userPost.as_view()),
    path('userupdate/',userView.userUpdate.as_view()),
    path('userdelete/<int:id>/',userView.userDelete.as_view()),
    path('roleget/<int:id>/',userView.roleGet.as_view()),
    path('rolegetall/',userView.roleGetAll.as_view()),
    path('rolecreate/',userView.rolePost.as_view()),
    path('roleupdate/',userView.roleUpdate.as_view()),
    path('roledelete/<int:id>/',userView.roleDelete.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', userView.login.as_view()),
    # path('api/login/', users.views.CustomLoginView.as_view(), name='login'),
]
