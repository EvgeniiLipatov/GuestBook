from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Имя автора')
    email = forms.EmailField(max_length=70, required=True, label='email автора')
    text = forms.CharField(max_length=1500, required=True, label='Текст записи',widget=widgets.Textarea)