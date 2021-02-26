from django.urls import path
from . import views

urlpatterns = [
    path('list', views.BarangList.as_view(), name='barang_list'),
    path('add', views.BarangAdd.as_view(), name='barang_add'),
    path('edit/<int:pk>', views.BarangUpdate.as_view(), name='barang_edit'),
    path('delete/<int:pk>', views.BarangDelete, name='barang_delete'),

    path('inv_list', views.InventoryList.as_view(), name='inventaris_list'),
    path('inv_add', views.InventoryAdd.as_view(), name='inventaris_add'),
    path('inv_edit/<int:pk>', views.InventoryUpdate.as_view(), name='inventaris_edit'),
    path('inv_delete/<int:pk>', views.InventoryDelete, name='inventaris_delete'),
]