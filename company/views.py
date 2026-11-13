from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, AboutStats, HomeStats, HomeServices, WhyUs, Services, Reviews

# Create your views here.

def home(request):
    home_stats = HomeStats.objects.all()
    home_services = HomeServices.objects.all()
    why_us = WhyUs.objects.all()
    reviews = Reviews.objects.all()

    context = {
            'home_stats': home_stats,
            'home_services': home_services,
            'why_us': why_us,
            'reviews': reviews
        }

    return render(request, 'home.html', context=context)

def about(request):
    team = Team.objects.all()
    about_stats = AboutStats.objects.all()

    context = {
        'team': team,
        'about_stats': about_stats,
    }
    return render(request, 'about.html', context=context)

def service(request):
    services = Services.objects.all()

    context = {
        'services': services
    }
   
    return render(request, 'service.html', context=context)

def contact(request):
    return render(request, 'contact.html')

def service_detail(request, pk):
    service = Services.objects.get(id=pk)
    context = {
            'services': service
        }
    print(service)
    return render(request, 'service-detail.html', context=context)