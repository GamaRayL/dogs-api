from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from main.models import Dog, Breed


class BreedListSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)


class BreedDetailSerializer(ModelSerializer):
    dogs_this_breed = SerializerMethodField()

    @staticmethod
    def get_dogs_this_breed(breed):
        if Dog.objects.filter(breed=breed):
            return [dog.name for dog in Dog.objects.filter(breed=breed)]
        else:
            return None

    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class DogListSerializer(ModelSerializer):
    breed = SlugRelatedField(slug_field='name', queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ('name', 'breed')


class DogDetailSerializer(ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()

    @staticmethod
    def get_dog_with_same_breed(dog):
        return Dog.objects.filter(breed=dog.breed).count()

    class Meta:
        model = Dog
        fields = ('name', 'breed', 'dog_with_same_breed')