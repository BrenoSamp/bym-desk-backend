from django.contrib import admin
from bym_desk_app.models import Usuario, Analista

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
