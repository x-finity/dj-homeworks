from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponseNotFound


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = [book for book in Book.objects.all()]
    # for book in books:
    #     book.pub_date = book.pub_date.strftime('%Y-%m-%d')
    context = {"books": books}
    return render(request, template, context)


def book_by_pub_date(request, pub_date):
    def get_dict_from_books(books):
        n = 0
        date = {}
        for book in books:
            if book.pub_date.strftime('%Y-%m-%d') not in date.values():
                date[n] = book.pub_date.strftime('%Y-%m-%d')
                n += 1
        return date
    template = 'books/book.html'
    try:
        books = [book for book in Book.objects.filter(pub_date=pub_date)]
    except Book.DoesNotExist:
        return HttpResponseNotFound('Такой книги нет')
    dates = get_dict_from_books(Book.objects.order_by('pub_date'))
    current_page = list(filter(lambda x: dates[x] == pub_date.strftime('%Y-%m-%d'), dates))[0]
    if current_page != 0:
        prev = dates[current_page-1]
    else:
        prev = None
    if current_page != len(dates)-1:
        next = dates[current_page+1]
    else:
        next = None
    context = {
        "books": books,
        "page": books,
        "prev": prev,
        "next": next
    }
    return render(request, template, context)