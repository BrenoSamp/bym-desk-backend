from django.contrib import admin
from bym_desk_app.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha', 'telefone')
    list_display_links = ('id', 'nome', 'email', 'senha', 'telefone')
    search_fields = ('id', 'nome', 'email',  'senha', 'telefone')

admin.site.register(Usuario, Usuarios)
