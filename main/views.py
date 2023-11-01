from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from main.models import Dog, Breed
from main.serializers import DogSerializer, DogListSerializer, BreedDetailSerializer, DogDetailSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedDetailSerializer


class DogListAPIView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class DogDetailAPIView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer


class DogUpdateAPIView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()
