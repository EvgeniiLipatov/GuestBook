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
            Book.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )

            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def update_record_view(request, pk):
    record = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={
            'author': record.author,
            'email': record.email,
            'text': record.text
        })
        return render(request, 'update.html', context={
            'form': form,
            'record': record
        })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data['author']
            record.email = form.cleaned_data['email']
            record.text = form.cleaned_data['text']
            record.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form})


def delete_record_view(request, pk):
    record = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'record': record
        })
    elif request.method == 'POST':
        record.delete()
        return redirect('index')
