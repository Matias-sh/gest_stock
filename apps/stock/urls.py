from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    #------------------------------------------- Inventario -------------------------------------------
    path('inventario/', inventario_list, name='inventario_list'),
    path('inventario/new_inventario/', inventario_create, name='new_inventario'),
    path('inventario/update_inventario/<int:id>/', inventario_update, name='update_inventario'),
    path('inventario/delete_inventario/<int:id>/', inventario_delete, name='delete_inventario'),
    #------------------------------------------- Articulos -------------------------------------------
    path('articulos/', articulo_list, name='articulo_list'),
    path('articulos/new_articulo/', articulo_create, name='new_articulo'),
    path('articulos/update_articulo/<int:id>/', articulo_update, name='update_articulo'),
    path('articulos/delete_articulo/<int:id>/', articulo_delete, name='delete_articulo'),
    # Marcas
    path('marcas/', marcas_list, name='marcas_list'),
    path('marcas/new_marcas/', marcas_create, name='new_marcas'),
    path('marcas/update_marcas/<int:id>/', marcas_update, name='update_marcas'),
    path('marcas/delete_marcas/<int:id>/', marcas_delete, name='delete_marcas'),
    # Tipo de Articulos
    path('tpo_articulos/', tpo_articulos_list, name='tpo_articulos_list'),
    path('tpo_articulos/new_tpo_articulos/', tpo_articulos_create, name='new_tpo_articulos'),
    path('tpo_articulos/update_tpo_articulos/<int:id>/', tpo_articulos_update, name='update_tpo_articulos'),
    path('tpo_articulos/delete_tpo_articulos/<int:id>/', tpo_articulos_delete, name='delete_tpo_articulos'),
    #------------------------------------------- MOVIMIENTOS -------------------------------------------
    path('movimientos/', movimientos_list, name='movimientos_list'),
    path('movimientos/new_movimientos/', movimientos_create, name='new_movimientos'),
    path('movimientos/update_movimientos/<int:id>/', movimientos_update, name='update_movimientos'),
    path('movimientos/delete_movimientos/<int:id>/', movimientos_delete, name='delete_movimientos'),
    # Tipo Movimientos
    path('tpo_movimientos/', tpo_mov_list, name='tpo_mov_list'),
    path('tpo_movimientos/new_tpo_mov/', tpo_mov_create, name='new_tpo_mov'),
    path('tpo_movimientos/update_tpo_mov/<int:id>/', tpo_mov_update, name='update_tpo_mov'),
    path('tpo_movimientos/delete_tpo_mov/<int:id>/', tpo_mov_delete, name='delete_tpo_mov'),
]
