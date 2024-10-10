from rest_framework import serializers
from .models import *


class BachatGatRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BachatGatRegistration
        fields = '__all__'


class MemberRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberRegistration
        fields = '__all__'