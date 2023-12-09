"""
URL configuration for finalProjectKiraSelucky project.

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
from django.urls import include, path, re_path
from dnd.views import index
from django.contrib.auth import views as auth_views
from dnd.views import register

urlpatterns = [
    path("dnd/", include("dnd.urls", namespace='dnd')),
    path("admin/", admin.site.urls),
    re_path(r"^$", index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]