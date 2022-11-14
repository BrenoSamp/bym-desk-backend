from django.http import JsonResponse
from rest_framework import viewsets
from bym_desk_app.models import Usuario
from bym_desk_app.serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def createUser(request):
    if request.method == 'POST':
        user = {'id': 1}
        return JsonResponse(user)
