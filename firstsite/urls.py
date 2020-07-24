"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import hello.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name="home"),
    path('new', hello.views.new, name="new"),
    path('create', hello.views.create, name="create"),
    path('detail/<int:post_id>', hello.views.detail, name="detail"),
    path('update/<int:post_id>', hello.views.update, name="update"),
    path('edit/<int:post_id>', hello.views.edit, name="edit"),
    path('delete/<int:post_id>', hello.views.delete, name="delete"),
]
