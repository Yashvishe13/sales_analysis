from django import forms
from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_gender': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        

        
        