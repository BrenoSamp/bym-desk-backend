from django.http import JsonResponse
from rest_framework import viewsets
from bym_desk_app.models import Usuario, Analista
from bym_desk_app.serializer import UsuarioSerializer, AnalistaSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class AnalistasViewSet(viewsets.ModelViewSet):
    queryset = Analista.objects.all()
    serializer_class = AnalistaSerializer

def createUser(request):
    if request.method == 'POST':
        user = {'id': 1}
        return JsonResponse(user)
