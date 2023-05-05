from django.shortcuts import render, redirect
from .models import *
from .forms import *

def dashboard(request):
    return render(request, 'bases/base.html')

# ARTICULOS FUNCTIONS

def articulo_list(request):
    articulos = Articulos.objects.all()

    context = {
        'articulos': articulos
    }

    return render(request, 'articulos/articulos_list.html', context)

def articulo_create(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulo_list')
    else:
        form = ArticuloForm()
    context = {
        'form': form
    }
    return render(request, 'bases/formulario.html', context)

def articulo_update(request, id):
    articulo = Articulos.objects.get(cod_articulo=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulo_list')
    else:
        form = ArticuloForm(instance=articulo)

    context = {
        'form': form
    }

    return render(request, 'bases/formulario.html', context)

def articulo_delete(request, id):
    articulo = Articulos.objects.get(cod_articulo=id)
    articulo.delete()
    return redirect('articulo_list')

# TIPO ARTICULOS FUNCTIONS

def tpo_articulos_list(request):
    tpo_articulos = Tpo_Articulos.objects.all()

    context = {
        'tpo_articulos': tpo_articulos
    }

    return render(request, 'articulos/tpo_articulos/tpo_articulos_list.html', context)

def tpo_articulos_create(request):
    if request.method == 'POST':
        form = TpoArtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tpo_articulos_list')
    else:
        form = TpoArtForm()
    context = {
        'form': form
    }
    return render(request, 'bases/formulario.html', context)

def tpo_articulos_update(request, id):
    tpo_art = Tpo_Articulos.objects.get(id_tpo_articulo=id)
    if request.method == 'POST':
        form = TpoArtForm(request.POST, instance=tpo_art)
        if form.is_valid():
            form.save()
            return redirect('tpo_articulos_list')
    else:
        form = TpoArtForm(instance=tpo_art)

    context = {
        'form': form
    }

    return render(request, 'bases/formulario.html', context)

def tpo_articulos_delete(request, id):
    tpo_art = Tpo_Articulos.objects.get(id_tpo_articulo=id)
    tpo_art.delete()
    return redirect('tpo_articulos_list')


# MARCAS FUNCTIONS

def marcas_list(request):
    marcas = Marcas.objects.all()

    context = {
        'marcas': marcas
    }

    return render(request, 'articulos/marcas/marcas_list.html', context)

def marcas_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcas_list')
    else:
        form = MarcaForm()
    context = {
        'form': form
    }
    return render(request, 'bases/formulario.html', context)

def marcas_update(request, id):
    marca = Marcas.objects.get(id_marca=id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marcas_list')
    else:
        form = MarcaForm(instance=marca)

    context = {
        'form': form
    }

    return render(request, 'bases/formulario.html', context)

def marcas_delete(request, id):
    marca = Marcas.objects.get(id_marca=id)
    marca.delete()
    return redirect('marcas_list')

# MOVIMIENTOS FUNCTIONS

def movimientos_list(request):
    movimientos = Movimientos.objects.all()
    context = {
        'movimientos': movimientos
    }

    return render(request, 'movimientos/movimientos_list.html', context)

def movimientos_create(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        tpo_mov = int(request.POST.get('id_tpo_movimiento'))
        if tpo_mov == 2:
            codigo_articulo = int(request.POST.get('cod_articulo'))
            articulo = Articulos.objects.get(cod_articulo=codigo_articulo)
            cantidad = articulo.stock - int(request.POST.get('cantidad'))
            Articulos.objects.filter(cod_articulo=codigo_articulo).update(stock=cantidad)
        elif tpo_mov == 1:
            codigo_articulo = int(request.POST.get('cod_articulo'))
            articulo = Articulos.objects.get(cod_articulo=codigo_articulo)
            cantidad = articulo.stock + int(request.POST.get('cantidad'))
            Articulos.objects.filter(cod_articulo=codigo_articulo).update(stock=cantidad)

        if form.is_valid():
            form.save()
            return redirect('movimientos_list')
    else:
        form = MovimientoForm()
    context = {
        'form': form
    }

    return render(request, 'bases/formulario.html', context)

def movimientos_update(request, id):
    movimiento = Movimientos.objects.get(id_movimiento=id)
    if request.method == 'POST':
        form = MovimientoForm(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            return redirect('movimientos_list')
    else:
        form = MovimientoForm(instance=movimiento)

    context = {
        'form': form
    }
    return render(request, 'bases/formulario.html', context)

def movimientos_delete(request, id):
    movimiento = Movimientos.objects.get(id_movimiento=id)
    if int(movimiento.id_tpo_movimiento.id_tpo_movimiento) == 2:
        codigo_articulo = movimiento.cod_articulo.cod_articulo
        articulo = Articulos.objects.get(cod_articulo=codigo_articulo)
        cantidad = articulo.stock + int(movimiento.cantidad)
        Articulos.objects.filter(cod_articulo=codigo_articulo).update(stock=cantidad)
        movimiento.delete()
    elif int(movimiento.id_tpo_movimiento.id_tpo_movimiento) == 1:
        codigo_articulo = movimiento.cod_articulo.cod_articulo
        articulo = Articulos.objects.get(cod_articulo=codigo_articulo)
        cantidad = articulo.stock - int(movimiento.cantidad)
        Articulos.objects.filter(cod_articulo=codigo_articulo).update(stock=cantidad)
        movimiento.delete()
    return redirect('movimientos_list')

# TIPO DE MOVIMIENTOS

def tpo_mov_list(request):
    tpos = Tpo_Movimientos.objects.all()

    context = {
        'tpos': tpos
    }

    return render(request, 'movimientos/tpo_movimientos/tpo_mov_list.html', context)

def tpo_mov_create(request):
    if request.method == 'POST':
        form = TpoMovForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tpo_mov_list')
    else:
        form = TpoMovForm()
    context = {
        'form': form
    }
    return render(request, 'bases/formulario.html', context)

def tpo_mov_update(request, id):
    tpo = Tpo_Movimientos.objects.get(id_tpo_movimiento=id)
    if request.method == 'POST':
        form = TpoMovForm(request.POST, instance=tpo)
        if form.is_valid():
            form.save()
            return redirect('tpo_mov_list')
    else:
        form = TpoMovForm(instance=tpo)

    context = {
        'form': form
    }

    return render(request, 'bases/formulario.html', context)

def tpo_mov_delete(request, id):
    tpo = Tpo_Movimientos.objects.get(id_tpo_movimiento=id)
    tpo.delete()
    return redirect('tpo_mov_list')


# ARTICULO VIEWS
"""
class ArticuloListView(ListView):
    model = Articulos
    template_name = 'stock/articulo_list.html'

class ArticuloCreateView(CreateView):
    model = Articulos
    template_name = 'stock/articulo_form.html'
    fields = '__all__'


class ArticuloUpdateView(UpdateView):
    model = Articulos
    template_name = 'stock/articulo_form.html'
    fields = '__all__'


class ArticuloDeleteView(DeleteView):
    model = Articulos
    template_name = 'stock/articulo_confirm_delete.html'

    def get_success_url(self):
        return reverse('articulo_list')
"""
# INGRESO VIEWS
"""
class IngresoListView(ListView):
    model = Ingresos
    template_name = 'stock/ingreso_list.html'

class IngresoCreateView(CreateView):
    model = Ingresos
    template_name = 'stock/ingreso_form.html'
    fields = '__all__'

    def ingreso_create(self):
        total_articulos = Articulo.objects.count()
        stock_create = Articulo.objects.aggregate(stocks=Sum('stock'))['stocks']
        total_stock = Articulo.objects.aggregate(total=Sum('stock_actual'))['total']


    def form_valid(self, form):
        ingreso = form.save(commit=False)
        ingreso.save()

        detalles = self.request.POST.getlist('detalles_de_ingreso')
        for detalle in detalles:
            articulo_id, cantidad = detalle.split('-')
            articulo = get_object_or_404(Articulos, pk=articulo_id)
            detalle_ingreso = DetalleIngreso(
                articulo=articulo,
                cantidad=cantidad,
                ingreso=ingreso,
            )
            detalle_ingreso.save()
            articulo.stock_actual += int(cantidad)
            articulo.save()

        return super().form_valid(form)

        
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'stock/articulo_list.html'


class ArticuloCreateView(CreateView):
    model = Articulo
    template_name = 'stock/articulo_form.html'
    fields = '__all__'


class ArticuloUpdateView(UpdateView):
    model = Articulo
    template_name = 'stock/articulo_form.html'
    fields = '__all__'


class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'stock/articulo_confirm_delete.html'

    def get_success_url(self):
        return reverse('articulo_list')


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'stock/articulo_detail.html'


class IngresoListView(ListView):
    model = Ingreso
    template_name = 'stock/ingreso_list.html'

class IngresoCreateView(CreateView):
    model = Ingreso
    template_name = 'stock/ingreso_form.html'
    fields = ['fecha']

    def form_valid(self, form):
        ingreso = form.save(commit=False)
        ingreso.save()

        detalles = self.request.POST.getlist('detalles_de_ingreso')
        for detalle in detalles:
            articulo_id, cantidad = detalle.split('-')
            articulo = get_object_or_404(Articulo, pk=articulo_id)
            detalle_ingreso = DetalleIngreso(
                articulo=articulo,
                cantidad=cantidad,
                ingreso=ingreso,
            )
            detalle_ingreso.save()
            articulo.stock_actual += int(cantidad)
            articulo.save()

        return super().form_valid(form)



class IngresoDetailView(DetailView):
    model = Ingreso
    template_name = 'stock/ingreso_detail.html'


class EgresoListView(ListView):
    model = Egreso
    template_name = 'stock/egreso_list.html'


class EgresoCreateView(CreateView):
    model = Egreso
    template_name = 'stock/egreso_form.html'
    fields = '__all__'


class EgresoDetailView(DetailView):
    model = Egreso
    template_name = 'stock/egreso_detail.html'


class DetalleIngresoCreateView(CreateView):
    model = DetalleIngreso
    template_name = 'stock/detalle_ingreso_form.html'
    fields = '__all__'


class DetalleEgresoCreateView(CreateView):
    model = DetalleEgreso
    template_name = 'stock/detalle_egreso_form.html'
    fields = '__all__'

def dashboard(request):
    total_articulos = Articulo.objects.count()
    total_stock = Articulo.objects.aggregate(total=Sum('stock_actual'))['total']
    ultimos_ingresos = Ingreso.objects.order_by('-fecha')[:5]
    ultimos_egresos = Egreso.objects.order_by('-fecha')[:5]
    return render(request, 'stock/dashboard.html', {
        'total_articulos': total_articulos,
        'total_stock': total_stock,
        'ultimos_ingresos': ultimos_ingresos,
        'ultimos_egresos': ultimos_egresos
    })

"""
