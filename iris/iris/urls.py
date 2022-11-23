"""iris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from irisjs import views

urlpatterns = [
    path('admin/', admin.site.urls), #caminho /admin/ nos levará à página do administrador
    path('', views.HomeView.as_view()), #homepage da nossa aplicação web. Dentro de views, irá usar a classe HomeView para abrir a página .html (index.html). Essa classe será implementada a seguir
    path('api', views.ListIris.as_view()) #api onde serão armazenados nossos dados estruturados para criação dos gráficos. Será definido depois
]
