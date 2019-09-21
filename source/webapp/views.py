from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Book, STATUS_CHOICES


def index_view(request, *args, **kwargs):
    records = Book.objects.filter(status="active").order_by('-CreatedDate')
    return render(request, 'index.html', context={
        'records': records
    })
