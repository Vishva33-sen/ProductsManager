from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.
def home(request):
    return render(request, 'home.html')

def myapp(request,t):
    product = Product.objects.filter(type=t)  # Example to get a product
    # product = get_object_or_404(Product, pk=product.id)  # Example to get a product with primary key 1
    return render(request, 'myapp.html', {'product': product,'type':t})

def getTypes(request):
    types = Product.objects.values_list('type', flat=True).distinct()
    return render(request, 'types.html', {'types': types})
