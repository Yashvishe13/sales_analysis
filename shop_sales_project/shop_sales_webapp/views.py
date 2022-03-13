from django.shortcuts import redirect, render
from . models import Customer
from . forms import CustomerForm

def index(request):
    customers = Customer.objects.all()
    
    form = CustomerForm(request.POST)
        
    context = {
        "customers" : customers,
        "form" : form,
    }
    
    return render(request, 'shop_sales_webapp/index.html', context)

def data_entry(request):
    products = Customer.objects.all()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomerForm()
        
    context = {
        "form" : form,
    }
        
    return render(request, 'shop_sales_webapp/data_entry.html', context)
