from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from main.models import Dog, Breed
from main.services import get_currency_rate
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
        exclude = ['price']
        validators = [
            DogNameValidator(field='name')
        ]


class DogListSerializer(ModelSerializer):
    breed = SlugRelatedField(slug_field='name', queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed')


class DogDetailSerializer(ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()
    price_usd = SerializerMethodField()
    price_eur = SerializerMethodField()

    @staticmethod
    def get_price_usd(obj):
        currency = get_currency_rate('usd')
        amount = int(obj.price / currency)
        return amount if currency else None

    @staticmethod
    def get_price_eur(obj):
        currency = get_currency_rate('eur')
        amount = int(obj.price / currency)
        return amount if currency else None

    @staticmethod
    def get_dog_with_same_breed(obj):
        return Dog.objects.filter(breed=obj.breed).count()

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'is_public', 'dog_with_same_breed', 'price',
                  'price_usd', 'price_eur')
