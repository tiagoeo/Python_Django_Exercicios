from django.shortcuts import render
from .models import produto

def inicio(request):
    rel_produto = produto.objects.all()
    return render(request, 'produtos.html', {'rel_produto':rel_produto})