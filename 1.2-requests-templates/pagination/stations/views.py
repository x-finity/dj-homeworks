from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from csv import DictReader
from pprint import pprint

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        stations = list(DictReader(file, delimiter=','))
        # pprint(list(stations))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 10)
    bus_stations = paginator.get_page(page_number)
    context = {
        'bus_stations': bus_stations,
        'page': bus_stations,
    }
    return render(request, 'stations/index.html', context)
