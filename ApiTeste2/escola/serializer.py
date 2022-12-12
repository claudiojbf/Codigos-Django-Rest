from logging import exception
from rest_framework import serializers

from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'cpf': {'write_only':True}
        }
        model=Aluno
        fields = ('id', 'nome', 'cpf')

