from django.shortcuts import redirect, render
from . models import Product
from . forms import ProductForm

def index(request):

    products = Product.objects.all()
    
    form = ProductForm(request.POST)
        
    context = {
        "products" : products,
        "form" : form,
    }
    
    return render(request, 'grow/index.html', context)

def data_entry(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
        
    context = {
        "form" : form,
    }
        
    return render(request, 'grow/data_entry.html', context)
