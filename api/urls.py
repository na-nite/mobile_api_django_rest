from django.contrib import admin
from django.urls import path

from rest_framework import routers

from api.views import CountryList, SlideShowList, VedioList

router = routers.SimpleRouter()
router.register(r'countries', CountryList)
router.register(r'slideshowImages', SlideShowList)
router.register(r'vedios', VedioList)

urlpatterns = router.urls
