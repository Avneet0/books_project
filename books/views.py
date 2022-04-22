from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Books
from django.db.models import Q
class BookListView(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchResultsListView(ListView): # new
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        return Books.objects.filter(
            Q(title__icontains='money') | Q(title__icontains='api')
        )