from rest_framework import serializers

from country.models import Country, SlideShowImages


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['pk',
                  'name',
                  'capital',
                  'description',
                  'surface',
                  'population',
                  'historique',
                  'ressources',
                  'personnalités',
                  'drapeau',
                  'hymne',
                  'drapeau_carre']


class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideShowImages
        fields = ['pk',
                  'image',
                  'country',
                  'title']


class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideShowImages
        fields = ['pk',
                  'file',
                  'country',]
