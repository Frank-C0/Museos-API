# change login serializer with token, email and username
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from dj_rest_auth.serializers import TokenSerializer
from rest_framework import serializers

class CustomTokenSerializer(TokenSerializer):
    # Sobreescribe el serializador para incluir email y username
    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'email', 'username')