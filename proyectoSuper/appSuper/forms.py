from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['s_name', 'd_price', 'i_quantity']
    widgets = {
      's_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
      'd_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
      'i_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
    }

class ItemCheckboxForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['b_checked']
    widgets = {
      'b_checked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
