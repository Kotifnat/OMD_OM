from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Field
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken

from .models import CBU


class MyTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return AccessToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        access = self.get_token(self.user)
        data['access'] = str(access)
        return data


class CBUModelSerializer(ModelSerializer):
    class Meta:
        model = CBU
        fields = ('unit', 'reach',)

    def validate(self, data):
        if data['unit'] < 0:
            raise ValidationError({'unit': "Значение должно быть больше 0!"})
        if data['reach'] != sorted(data['reach'], reverse=True):
            raise ValidationError({'reach': 'Значения должны убывать!'})
        if len(data['reach']) != 10:
            raise ValidationError({'reach': 'Должно быть 10 значений!'})
        if any(i < 0 or i > 100 for i in data['reach']):
            raise ValidationError({'reach': 'Охват не может быть менее 0 или более 100%'})
        return data
