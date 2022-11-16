from rest_framework import serializers
from bym_desk_app.models import Usuario, Analista, Ticket

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AnalistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analista
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ListaTicketsUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ListaTicketsAnalistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'