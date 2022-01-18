from rest_framework import serializers

from apps.grants.models import Category, Grant, Location, Discipline


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = ('id', 'name', 'desc',
                  'organization', 'location',
                  'discipline', 'duration',
                  'deadline', 'category', 'img')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name')
