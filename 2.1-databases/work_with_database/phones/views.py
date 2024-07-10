from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = [phone for phone in Phone.objects.order_by('name')]
    elif sort == 'min_price':
        phones = [phone for phone in Phone.objects.order_by('price')]
    elif sort == 'max_price':
        phones = [phone for phone in Phone.objects.order_by('-price')]
    else:
        phones = [phone for phone in Phone.objects.all()]
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except Phone.DoesNotExist:
        return HttpResponseNotFound('Такого телефона нет')
    context = {"phone": phone}
    return render(request, template, context)
