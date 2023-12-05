from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password

        return token