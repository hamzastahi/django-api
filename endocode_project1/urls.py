"""endocode_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import url, include
import subprocess 

@api_view(['GET','POST'])
def helloworld(request):
    if request.method == 'POST':
         name = request.GET.get("name")
         if name is None:
             name = "Stranger"
         return Response('Hello {}!'.format(name))
    return Response( "Hello Stranger!")

@api_view(['GET'])
def get_git_info(request):
    label = subprocess.check_output(["git", "describe","--always"]).strip()
    return Response({'GitHash': label, 'Project Name': 'endocode'})
 
        

urlpatterns = [
  url(r'helloworld', helloworld),
  url(r'versionz', get_git_info)
  
]