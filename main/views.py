from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from main.models import Dog, Breed
from main.permissions import IsOwnerOrStaff
from main.serializers import DogSerializer, DogListSerializer, BreedDetailSerializer, DogDetailSerializer, \
    BreedSerializer, BreedListSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    default_serializer = BreedSerializer
    serializes = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,

    }

    def get_serializer_class(self):
        return self.serializes.get(self.action, self.default_serializer)


class DogListAPIView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class DogDetailAPIView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permission_classes = [IsOwnerOrStaff]


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer


class DogUpdateAPIView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()


