from django.contrib import admin

# Register your models here.
from country.models import Country, SlideShowImages, Vedios

admin.site.register(Country)
admin.site.register(SlideShowImages)
admin.site.register(Vedios)
