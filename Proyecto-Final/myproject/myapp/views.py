from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from django.db.models import Q

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
        
        if query:
            # Realiza una búsqueda en todas las tablas y campos relevantes
            categorias = Categoria.objects.filter(
                Q(nombre__icontains=query)
            )
            
            productos = Producto.objects.filter(
                Q(nombre__icontains=query) |
                Q(categoria__nombre__icontains=query) |  # Asumiendo que categoria es una ForeignKey en Producto
                Q(precio__icontains=query)
            )
            
            clientes = Cliente.objects.filter(
                Q(nombre__icontains=query) |
                Q(direccion__icontains=query) |
                Q(email__icontains=query)
            )
            
            return render(request, 'search_results.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})
        else:
            # Handle the case where the query is None (or empty) as needed
            return render(request, 'search_results.html', {'categorias': [], 'productos': [], 'clientes': []})