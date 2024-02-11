from rest_framework import serializers
from pharma.models import Cure


class CureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cure
        fields = '__all__'
