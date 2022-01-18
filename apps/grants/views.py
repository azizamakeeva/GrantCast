from rest_framework.viewsets import ModelViewSet

from apps.grants.models import Category, Grant, Location, Discipline
from apps.grants.serializers import CategorySerializer, GrantSerializer, LocationSerializer, DisciplineSerializer


class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GrantAPIViewSet(ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer


class LocationAPIViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DisciplineAPIViewSet(ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
