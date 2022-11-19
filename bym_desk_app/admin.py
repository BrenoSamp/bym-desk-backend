from django.contrib import admin
from bym_desk_app.models import Usuario, Analista, Ticket, Mensagem

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha', 'telefone')
    list_display_links = ('id', 'nome', 'email', 'senha', 'telefone')
    search_fields = ('id', 'nome', 'email',  'senha', 'telefone')

admin.site.register(Usuario, Usuarios)

class Analistas(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'setor')
    list_display_links = ('id', 'matricula', 'setor')
    search_fields = ('id', 'matricula', 'setor')

admin.site.register(Analista, Analistas)

class Tickets(admin.ModelAdmin):
    list_display = ('id', 'solicitante_id', 'analista_id', 'bloco', 'local', 'tipo', 'data')
    list_display_links = ('id', 'solicitante_id', 'analista_id', 'bloco', 'local', 'tipo', 'data')
    search_fields = ('id', 'solicitante_id', 'analista_id', 'bloco', 'local', 'tipo', 'data')
    ordering = ('id',)

admin.site.register(Ticket, Tickets)

class Mensagens(admin.ModelAdmin):
    list_display = ('id', 'ticket_id', 'mensagem', 'imagem')
    list_display_links = ('id', 'ticket_id', 'mensagem', 'imagem')
    search_fields = ('id', 'ticket_id', 'mensagem', 'imagem')


admin.site.register(Mensagem, Mensagens)