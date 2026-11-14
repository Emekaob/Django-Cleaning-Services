
from .models import CompanyInfo  # Example if pulling from a database

def global_site_data(request):
   return {
       'coy': CompanyInfo.objects.all().first(),
   }