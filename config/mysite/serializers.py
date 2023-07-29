from rest_framework import serializers
from mysite.models import Quadro

class QuadroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadro
        fields = '__all__'
