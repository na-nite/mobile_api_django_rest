from rest_framework import generics, mixins, viewsets

from api.serializers import CountrySerializer, SlideShowSerializer, VedioSerializer
from country.models import Country, SlideShowImages, Vedios
from django_filters.rest_framework import DjangoFilterBackend


class CountryList(generics.ListAPIView, mixins.RetrieveModelMixin, viewsets.ViewSet):
    lookup_field = 'pk'
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class SlideShowList(generics.ListAPIView, viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
    serializer_class = SlideShowSerializer
    queryset = SlideShowImages.objects.all()


class VedioList(generics.ListAPIView, viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
    serializer_class = VedioSerializer
    queryset = Vedios.objects.all()
