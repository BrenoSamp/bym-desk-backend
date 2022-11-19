from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, generics, filters
from bym_desk_app.models import Usuario, Analista, Ticket
from bym_desk_app.serializer import UsuarioSerializer, AnalistaSerializer, TicketSerializer, ListaTicketsUsuarioSerializer, ListaTicketsAnalistaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
import json

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['id', 'nome', 'email',  'senha', 'telefone']
    filterset_fields = ['id', 'nome', 'email',  'senha', 'telefone']
class AnalistasViewSet(viewsets.ModelViewSet):
    queryset = Analista.objects.all()
    serializer_class = AnalistaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['id', 'matricula', 'setor']
    filterset_fields = ['id', 'matricula', 'setor']

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id', 'solicitante_id', 'analista_id', 'bloco', 'local', 'tipo', 'data']

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

@csrf_exempt
def createAnalista(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usuario = {
            'nome': body['nome'],
            'email': body['email'],
            'senha': body['senha'],
            'telefone': body['telefone'],
        }
        userSerializer = UsuarioSerializer(data=usuario)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        analista = {
            'matricula': body['matricula'],
            'setor': body['setor'],
            'usuario_id': userSerializer.data['id']
        }
        analistaSerializer = AnalistaSerializer(data=analista)
        analistaSerializer.is_valid(raise_exception=True)
        analistaSerializer.save()

        analistaFormatted = {
            'id': userSerializer.data['id'],
            'nome': body['nome'],
            'email': body['email'],
            'senha': body['senha'],
            'telefone': body['telefone'],
            'analista_id': analistaSerializer.data['id'],
            'matricula': body['matricula'],
            'setor': body['setor']
        }

        return JsonResponse(analistaFormatted)
