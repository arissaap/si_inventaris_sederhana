from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventaris.models import Barang, Inventaris


def dashboard(request):
    return render(request, 'index.html',{})

@method_decorator(login_required, name='dispatch')
class BarangList(ListView):
    model = Barang
    context_object_name = 'data'

@method_decorator(login_required, name='dispatch')
class BarangAdd(CreateView):
    model = Barang
    fields = '__all__'
    success_url = reverse_lazy('barang_list')

@method_decorator(login_required, name='dispatch')
class BarangUpdate(UpdateView):
    model = Barang
    fields = '__all__'
    success_url = reverse_lazy('barang_list')

@login_required
def BarangDelete(request, pk):
    data = Barang.objects.get(pk = pk)
    data.delete()
    return redirect('barang_list')

########INVENTARIS########
@method_decorator(login_required, name='dispatch')
class InventoryList(ListView):
    model = Inventaris
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Inventaris.objects.all().aggregate(Sum('harga_pembelian'))
        return context

@method_decorator(login_required, name='dispatch')
class InventoryAdd(CreateView):
    model = Inventaris
    fields = '__all__'
    template_name = 'inventaris/barang_form.html'
    success_url = reverse_lazy('inventaris_list')

@method_decorator(login_required, name='dispatch')
class InventoryUpdate(UpdateView):
    model = Inventaris
    fields = '__all__'
    template_name = 'inventaris/barang_form.html'
    success_url = reverse_lazy('inventaris_list')

@login_required
def InventoryDelete(request, pk):
    data = Inventaris.objects.get(pk = pk)
    data.delete()
    return redirect('inventaris_list')