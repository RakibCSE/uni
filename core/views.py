from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import View
from .forms import ContactForm, BookForm


class Index(View):
    """
    index page view
    """

    def get(self, request, *args, **kwargs):

        contact_form = ContactForm
        book_form = BookForm

        context = {
            'contact_form': contact_form,
            'book_form': book_form
        }
        return render(request, 'core/index.html', context)

    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(request.POST)
        book_form = BookForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            message = contact_form.cleaned_data.get('message')
            send_mail(
                f'{name}-{email} from ProfessorUni',  # subject
                message,  # message
                email,  # from email
                ['info@professoruni.com'],  # to email
            )
            messages.success(request, f'Hey {name}! Your message has been sent')
            return redirect('index')

        if book_form.is_valid():
            book_form.save()
            name = book_form.cleaned_data.get('name_b')
            email = book_form.cleaned_data.get('email_b')
            phone = book_form.cleaned_data.get('phone_b')
            comments = book_form.cleaned_data.get('comments_b')
            send_mail(
                f'{name}, {email}, {phone} from ProfessorUni',  # subject
                comments,  # message
                email,  # from email
                ['info@professoruni.com'],  # to email
            )
            messages.success(request, f'Hey {name}! Your message has been sent')
            return redirect('index')
