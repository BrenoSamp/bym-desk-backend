import datetime
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, generics, filters
from bym_desk_app.models import Usuario, Analista, Ticket, Mensagem, Bloco, Local, Matricula
from bym_desk_app.serializer import UsuarioSerializer, AnalistaSerializer, TicketSerializer, ListaTicketsUsuarioSerializer, MensagemSerializer, ListaMensagensTicketSerializer, BlocoSerializer, LocalSerializer, MatriculaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from bym_desk_app.producer import publish

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
    filterset_fields = ['id', 'solicitante_id', 'analista_id', 'local_id', 'tipo', 'data']

class BlocosViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id', 'nome']

class LocaisViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id', 'nome', 'bloco_id']

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id', 'matricula']

class ListaTicketsUsuarioViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Ticket.objects.filter(solicitante_id=self.kwargs['solicitante_id'])
        return queryset
    serializer_class= ListaTicketsUsuarioSerializer

@csrf_exempt
def createAnalista(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        matricula = Matricula.objects.filter(matricula=body['matricula'])

        if matricula.exists() == False:
            error = {
                'error': 'Matricula não existe'
            }

            return JsonResponse(error)

        usuario = {
            'nome': body['nome'],
            'email': body['email'],
            'senha': body['senha'],
            'telefone': body['telefone'],
            'role': body['role'],
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
            'telefone': body['telefone'],
            'role': body['role'],
            'analista_id': analistaSerializer.data['id'],
            'matricula': body['matricula'],
            'setor': body['setor']
        }

        return JsonResponse(analistaFormatted)

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usuario = {
            'nome': body['nome'],
            'email': body['email'],
            'senha': body['senha'],
            'telefone': body['telefone'],
            'role': body['role'],
        }
        userSerializer = UsuarioSerializer(data=usuario)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        userFormatted = {
            'id': userSerializer.data['id'],
            'nome': body['nome'],
            'email': body['email'],
            'telefone': body['telefone'],
            'role': body['role']
        }

        return JsonResponse(userFormatted)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usuario = Usuario.objects.filter(email=body['email'], senha=body['senha'])

        if usuario.exists():
            usuario = Usuario.objects.get(email=body['email'], senha=body['senha'])
            serializedUser = {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email,
                'telefone': usuario.telefone,
                'role': usuario.role,
            }
            return JsonResponse(serializedUser)
        else:
            return JsonResponse({
                'error': 'E-mail ou senha incorreta'
            })

def listTicketsSolicitante(request):
    if request.method == 'GET':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usuarioFiltered = Usuario.objects.filter(id=body['usuario_id'])

        if usuarioFiltered.exists() == False:
            error = {
                'error': 'Solicitante não existe'
            }

            return JsonResponse(error)

        usuario = Usuario.objects.get(id=body['usuario_id'])

        q = Q()

        if body['id']:
            q &= Q(id=body['id'])
        q &= Q(solicitante_id=usuario.id)
        ticket = Ticket.objects.get(q)
        local = Local.objects.get(local_id=ticket.local_id)
        bloco = Bloco.objects.get(id=local.bloco_id)

        formattedResult = {
            'id': ticket.id,
            'solicitante_id': ticket.solicitante_id,
            'analista_id': ticket.analista_id,
            'local_id': ticket.local_id,
            'nome_local': local.nome,
            'bloco_id: ': local.bloco_id,
            'nome_bloco': bloco.nome,
            'status': ticket.status,
            'tipo': ticket.tipo,
            'data': ticket.data
        }

        return JsonResponse(formattedResult)

@csrf_exempt
def criaTicket(request):
    if request.method == 'POST':
        publish({'nome': 'Breno', 'email': 'bsampaio8@hotmail.com', 'setor':'Frigorifico'})
    return JsonResponse({})



def listTicketsAnalista(request):
    if request.method == 'GET':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        analista = Analista.objects.filter(id=body['analista_id'])

        q = Q()

        if analista.exists():
            analista = Analista.objects.get(id=body['analista_id'])
            if body['id']:
                q &= Q(id=body['id'])
            if body['status']:
                q &= Q(status=body['status'])
            ticket = Ticket.objects.get(q)
            local = Local.objects.get(local_id=ticket.local_id)
            bloco = Bloco.objects.get(id=local.bloco_id)

            formattedResult = {
                'id': ticket.id,
                'solicitante_id': ticket.solicitante_id,
                'analista_id': ticket.analista_id,
                'local_id': ticket.local_id,
                'nome_local': local.nome,
                'bloco_id: ': local.bloco_id,
                'nome_bloco': bloco.nome,
                'status': ticket.status,
                'tipo': ticket.tipo,
                'data': ticket.data
            }

            return JsonResponse(formattedResult)

        error = {
            'error': 'Analista não existe'
        }

        return JsonResponse(error)

class MensagensViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id', 'ticket_id', 'mensagem', 'imagem']

class ListaMensagensTicketViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Ticket.objects.filter(ticket_id=self.kwargs['ticket_id'])
        return queryset
    serializer_class= ListaMensagensTicketSerializer

def createTicket(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        current_date = datetime.date.today()

        ticket = {
            'solicitante_id': body['solicitante_id'],
            'tipo': body['tipo'],
            'local_id': body['local'],
            'status': 'em espera',
            'data': current_date
        }

        ticketSerializer = TicketSerializer(data=ticket)
        ticketSerializer.is_valid(raise_exception=True)
        ticketSerializer.save()

        ticketFormatted = {
            'id': ticketSerializer.data['id'],
            'solicitante_id': body['solicitante_id'],
            'tipo': body['tipo'],
            'local_id': body['local'],
            'status': 'em espera',
            'data': current_date
        }

        mensagem = {
            'ticket_id': ticketFormatted['id'],
            'mensagem': body['descricao']
        }

        mensagemSerializer = MensagemSerializer(data=mensagem)
        mensagemSerializer.is_valid(raise_exception=True)
        mensagemSerializer.save()

        publish({'nome': 'Matheus Henriques', 'email': 'math.marqui@gmail.com', 'setor':'Elétrico'})

        return JsonResponse(ticketFormatted)

def getBlocoLocal(request):
    if request.method == 'GET':
        locais_bloco = Local.objects.select_related('local', 'bloco')
        return locais_bloco