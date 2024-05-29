from django.shortcuts import render
from produtos.models import Celular

# Create your views here.
class Produto:
    def home(request):
        return render(request,'home.html')
    def list_products(request):
        celulares = Celular.objects.all()
        contex = {'celulares':celulares}
        return render(request,'list_products.html',contex)
        