from django import forms
from . models import Contact, Book


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name_b', 'email_b', 'phone_b', 'comments_b')
