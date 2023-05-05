from django.forms import ModelForm
from django import forms
from .models import *


class ArticuloForm(ModelForm):
    class Meta:
        
        model = Articulos

        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_tpo_articulo': forms.Select(attrs={'class': 'form-control'}),
            'id_marca': forms.Select(attrs={'class': 'form-control'}),
            'num_serie': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TpoArtForm(ModelForm):
    class Meta:

        model = Tpo_Articulos
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

class MarcaForm(ModelForm):
    class Meta:

        model = Marcas
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovimientoForm(ModelForm):
    class Meta:

        model = Movimientos

        fields = '__all__'

        widgets = {
            'id_tpo_movimiento': forms.Select(attrs={'class': 'form-control'}),
            'cod_articulo': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TpoMovForm(ModelForm):
    class Meta:

        model = Tpo_Movimientos
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }