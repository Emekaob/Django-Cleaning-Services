from django.contrib import admin
from .models import Team, AboutStats, HomeStats, HomeServices, WhyUs, Services, Reviews, CompanyInfo
# Register your models here.

admin.site.register(Team)
admin.site.register(AboutStats)
admin.site.register(HomeStats)
admin.site.register(HomeServices)
admin.site.register(WhyUs)
admin.site.register(Services)
admin.site.register(Reviews)
admin.site.register(CompanyInfo)