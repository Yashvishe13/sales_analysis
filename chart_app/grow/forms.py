from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        choices = ['bar', 'pie']
        model = Product
        fields = '__all__'
        widgets = {
            'date' : forms.TextInput(attrs={'class': 'form-control'}),
            'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer_gender': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        