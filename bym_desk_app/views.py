from django.http import JsonResponse
from rest_framework import viewsets, generics
from bym_desk_app.models import Usuario, Analista, Ticket
from bym_desk_app.serializer import UsuarioSerializer, AnalistaSerializer, TicketSerializer, ListaTicketsUsuarioSerializer, ListaTicketsAnalistaSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class AnalistasViewSet(viewsets.ModelViewSet):
    queryset = Analista.objects.all()
    serializer_class = AnalistaSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class ListaTicketsUsuarioViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Ticket.objects.filter(solicitante_id=self.kwargs['solicitante_id'])
        return queryset
    serializer_class= ListaTicketsUsuarioSerializer

class ListaTicketsAnalistaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Ticket.objects.filter(solicitante_id=self.kwargs['analista_id'])
        return queryset
    serializer_class = ListaTicketsAnalistaSerializer

def createUser(request):
    if request.method == 'POST':
        user = {'id': 1}
        return JsonResponse(user)
