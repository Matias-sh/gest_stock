from django.forms import ModelForm
from django import forms
from .models import *

class InventarioForm(ModelForm):
    class Meta:
        
        model = Inventario

        fields = '__all__'

        widgets = {
            'cod_articulo': forms.Select(attrs={'class': 'form-control'}),
            'num_serie': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'cod_articulo': 'Articulo:',
            'num_serie': 'Numero de Serie:',
            'modelo': 'Modelo:',
            'cantidad': 'Cantidad:',
        }


class ArticuloForm(ModelForm):

    class Meta:
        
        model = Articulos

        fields = ('nombre', 'id_tpo_articulo', 'id_marca')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tpo_articulo': forms.Select(attrs={'class': 'form-control'}),
            'id_marca': forms.Select(attrs={'class': 'form-control', 'value': ''}),
            'total_stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre': 'Nombre de Articulo:',
            'id_tpo_articulo': 'Tipo de Articulo:',
            'id_marca': 'Marca:',
        }

class TpoArtForm(ModelForm):
    class Meta:

        model = Tpo_Articulos
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'descripcion': 'Nombre del tipo de Articulo:',
        }

class MarcaForm(ModelForm):
    class Meta:

        model = Marcas
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }
        
        labels = {
            'descripcion': 'Nombre de la Marca del Articulo:',
        }


class MovimientoForm(ModelForm):
    class Meta:

        model = Movimientos

        fields = '__all__'

        widgets = {
            'id_tpo_movimiento': forms.Select(attrs={'class': 'form-control'}),
            'id_inventario': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'id_tpo_movimiento': 'Tipo de Movimiento:',
            'id_inventario': 'Inventario del Articulo:',
            'fecha': 'Fecha:',
            'observaciones': 'Observaciones:',
            'cantidad': 'Cantidad'
        }

class TpoMovForm(ModelForm):
    class Meta:

        model = Tpo_Movimientos
        
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'descripcion': 'Nombre del tipo de movimiento:',
        }