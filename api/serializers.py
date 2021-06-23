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


class ReachField(Field):

    def to_representation(self, value):
        value = [float(i) for i in value.reach.split(',')]
        return value

    def to_internal_value(self, data):
        self.validate_reach(data)
        return {"reach": ", ".join([str(i) for i in data])}

    @staticmethod
    def validate_reach(data):
        if data != sorted(data, reverse=True):
            raise ValidationError('Значения должны убывать!')
        if len(data) != 10:
            raise ValidationError('Должно быть 10 значений!')
        if any(i < 0 or i > 100 for i in data):
            raise ValidationError('Охват не может быть менее 0 или более 100%')


class CBUModelSerializer(ModelSerializer):
    reach = ReachField(source='*')

    class Meta:
        model = CBU
        fields = ('unit', 'reach',)

    def validate(self, data):
        if data['unit'] < 0:
            raise ValidationError({'unit': "Значение должно быть больше 0!"})
        return data
