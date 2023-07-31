from rest_framework import serializers
from mysite.models import Quadro,Tarefa

class QuadroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadro
        fields = '__all__'


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'