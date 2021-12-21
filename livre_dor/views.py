from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Card_model
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import Card_model_form

# Create your views here.

def display_livre_dor(request):
    if request.user.is_authenticated:
        all_books = Card_model.objects.order_by('-list_date')
        paginator = Paginator(all_books, 2)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        context = {
            'books': paged_listings
        }
        return render(request, 'livre_dor/livre.html', context)
    else:
        messages.error(request, 'You need to register first before go to RSVP')
        return render(request, 'accounts/register.html')


def display_livre_form(request):

    if request.method == "POST":
        form = Card_model_form(request.POST , request.FILES)
        if form.is_valid():
            curr = form.save(commit=False)
            curr.user = request.user
            curr.save()
            return redirect('http://127.0.0.1:8000/livre_dor/livre')

    return render(request,'livre_dor/livre_form.html')