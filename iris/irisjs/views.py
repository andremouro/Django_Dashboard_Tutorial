from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import File
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from django.db.models import Avg

class HomeView(View):  # definimos a classe HomeView que será chamada dentro do urls.py
    def get(self, request, *args, **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o index.html (que está dentro de irisjs)
        return render(request, 'irisjs/index.html')



class ListIris(APIView):  #criamos a classe que permitirá a criação da API
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):  #definimos o que esta classe irá retornar no API quando for requisitada (a estrutura dos dados)
        species = [iris.species for iris in File.objects.all()]  #neste caso, será criada uma variável 'species' em que estarão o nome das espécies de todas as linhas do nosso banco de dados (File)
        sepalLn = [iris.sepal_length for iris in File.objects.all()] # mesma coisa que o anterior, mas para o comprimento da sépala
        sepalWd = [iris.sepal_width for iris in File.objects.all()]  # mesma coisa que o anterior, mas para a largura da sépala
        speciesUnique = File.objects.values_list('species',flat=True).distinct()  #neste caso, estamos selecionando apenas os valores únicos de espécies
        spCount = File.objects.values('species').annotate(average_rating = Avg('sepal_length')).values_list('average_rating',flat=True)
        spScatter = [{'x':iris.sepal_length, 'y': iris.sepal_width} for iris in File.objects.all()]
        data = {"species":species,"sepalLn":sepalLn,"sepalWd":sepalWd, 'spUni':speciesUnique, 'spCount':spCount, 'spScatter':spScatter}
        return Response (data)

