from rest_framework import serializers
from bym_desk_app.models import Usuario, Analista

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AnalistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analista
        fields = '__all__'