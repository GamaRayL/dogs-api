from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.models import Dog, Breed
from main.paginations import DogPagination
from main.permissions import IsModerator, IsDogOwner, IsDogPublic
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
    permission_classes = [IsAuthenticated]
    # pagination_class = DogPagination


class DogDetailAPIView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permission_classes = [IsAuthenticated, IsModerator|IsDogOwner|IsDogPublic]


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]


class DogUpdateAPIView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated, IsModerator|IsDogOwner]


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]