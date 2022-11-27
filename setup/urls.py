"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bym_desk_app.views import UsuariosViewSet, AnalistasViewSet, TicketsViewSet, createAnalista, MensagensViewSet, ListaMensagensTicketViewSet, BlocosViewSet, LocaisViewSet, login, createUser, listTicketsAnalista, listTicketsSolicitante, MatriculasViewSet, criaTicket
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet, basename='Usuários')
router.register('analistas', AnalistasViewSet, basename='Analistas')
router.register('tickets', TicketsViewSet, basename='Tickets')
router.register('mensagens', MensagensViewSet, basename='Mensagens')
router.register('blocos', BlocosViewSet, basename='Blocos')
router.register('locais', LocaisViewSet, basename='Locais')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('login', login),
    path('admin/', admin.site.urls),
    path('analista/tickets', listTicketsAnalista),
    path('analista/create', createAnalista),
    path('solicitante/tickets', listTicketsSolicitante),
    path('solicitante/create', createUser),
    path('ticket/create', criaTicket),
    path('solicitante/<int:ticket_id>/mensagens', ListaMensagensTicketViewSet.as_view()),
]
