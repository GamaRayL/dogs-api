from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import BreedViewSet, DogListAPIView, DogDetailAPIView, DogCreateAPIView, DogDeleteAPIView, \
    DogUpdateAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'breed', BreedViewSet, basename='breed')

urlpatterns = [
    path('', DogListAPIView.as_view(), name='dogs'),
    path('<int:pk>/', DogDetailAPIView.as_view(), name='dog'),
    path('create/', DogCreateAPIView.as_view(), name='dog_create'),
    path('update/<int:pk>/', DogUpdateAPIView.as_view(), name='dog_update'),
    path('delete/<int:pk>/', DogDeleteAPIView.as_view(), name='dog_delete'),
              ] + router.urls
