from django.urls import path
from .views import home, about, service, contact, service_detail, footer, success_page

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('service/<int:pk>', service_detail, name='service_detail'),
    path('company_info', footer, name='company_info'),
    path('success_page', success_page, name='success_page'),

]