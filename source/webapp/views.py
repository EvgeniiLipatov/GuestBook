from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Book, STATUS_CHOICES
from webapp.forms import BookForm


def index_view(request, *args, **kwargs):
    records = Book.objects.filter(status="active").order_by('-CreatedDate')
    return render(request, 'index.html', context={
        'records': records
    })


def create_record_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            task = Book.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )

            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})
