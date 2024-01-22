from django.shortcuts import render, redirect
from .models import *


def index_view(request):
    context = {
        'portfolio': Portfolio.objects.last()
    }
    return render(request, 'index.html', context)


def create_contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
    return redirect("index_url")


def portfolio_detail_view(request):
    context = {
        'portfolio': PortfolioDetail.objects.last()
    }
    return render(request, 'portfolio-details.html', context)
