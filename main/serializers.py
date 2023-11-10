from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from main.models import Dog, Breed
from main.validators import DogNameValidator


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedListSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)


class BreedDetailSerializer(ModelSerializer):
    dogs_this_breed = SerializerMethodField()

    @staticmethod
    def get_dogs_this_breed(breed):
        if Dog.objects.filter(breed=breed):
            return DogListSerializer(Dog.objects.filter(breed=breed), many=True).data
        else:
            return None

    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
        validators = [
            DogNameValidator(field='name')
        ]


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
        fields = ('name', 'breed', 'is_public', 'dog_with_same_breed')
