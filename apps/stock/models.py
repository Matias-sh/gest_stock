from django.db import models

# ---------------------------------- Articulos ----------------------------------

class Tpo_Articulos(models.Model):
    id_tpo_articulo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion

class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Articulos(models.Model):
    cod_articulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_tpo_articulo = models.ForeignKey(Tpo_Articulos, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    total_stock = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('articulo_list')

    def __str__(self):
        txt = "{0} / {1}"
        return txt.format(self.nombre, self.id_marca)

# ---------------------------------- Inventario ----------------------------------

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cod_articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE, null=True)
    num_serie = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        txt = "{0}, modelo:{1}, N/S: {2}"
        return txt.format(self.cod_articulo.nombre, self.modelo, self.num_serie)

# ---------------------------------- Operaciones ----------------------------------

class Tpo_Movimientos(models.Model):
    id_tpo_movimiento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return self.descripcion

class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_tpo_movimiento = models.ForeignKey(Tpo_Movimientos, on_delete=models.CASCADE)
    id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_sistema = models.DateField(auto_now=True)
    observaciones = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        txt = "{0} de: {1}"
        return txt.format(self.id_tpo_movimiento, self.cod_articulo)





    