from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})

def add_data(request, model_name):
    if request.method == 'POST':
        form_class = {
            'categoria': CategoriaForm,
            'producto': ProductoForm,
            'cliente': ClienteForm,
        }[model_name.lower()]
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form_class = {
            'categoria': CategoriaForm,
            'producto': ProductoForm,
            'cliente': ClienteForm,
        }[model_name.lower()]
        form = form_class()

    return render(request, 'add_data.html', {'form': form, 'model_name': model_name})

def search_data(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query is not None:
            categorias = Categoria.objects.filter(nombre__icontains=query)
            productos = Producto.objects.filter(nombre__icontains=query)
            clientes = Cliente.objects.filter(nombre__icontains=query)
        else:
            categorias = []
            productos = []
            clientes = []

        context = {
            'categorias': categorias,
            'productos': productos,
            'clientes': clientes,
            'query': query,
        }

        return render(request, 'search_results.html', context)
