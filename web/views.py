from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Testimonial, Client, PortfolioCategory, PortfolioItem, Skill, Language, PostCategory, PostItem

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def index_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Xabar yuborildi. Javobni kuting!')
        else:
            field_errors = {field: error[0] for field, error in contact_form.errors.items()}
            for field, error in field_errors.items():
                messages.error(request, f'Notogri {field}: {error}')
    else:
        contact_form = ContactForm()

    context = {
        'testimonials': Testimonial.objects.all(),
        'clients': Client.objects.all().order_by('index'),
        'portfolio': {
            'categories': PortfolioCategory.objects.all().order_by('index'),
            'items': PortfolioItem.objects.all()
        },
        'skills': Skill.objects.all().order_by('index'),
        'languages': Language.objects.all().order_by('index'),
        'blog': {
            'categories': PostCategory.objects.all().order_by('index'),
            'posts': PostItem.objects.all()
        },
        'contact_form': contact_form,
        'age': calculate_age(datetime(2000, 12, 9))
    }

    return render(request, 'index.html', context)
