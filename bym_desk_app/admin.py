from django.contrib import admin
from bym_desk_app.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha')
    list_display_links = ('id', 'nome', 'email', 'senha')
    search_fields = ('id', 'nome', 'email',  'senha')

admin.site.register(Usuario, Usuarios)
