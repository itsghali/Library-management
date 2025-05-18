"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# D:\GHALI\3 AP\library_management\backend\library_management\urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from library.views import api_root


# Add a simple view for the root path
def redirect_to_api(request):
    return HttpResponseRedirect('/api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),     # DOIT venir avant include()
    path('api/', include('library.urls')),
    path('', redirect_to_api),
]
