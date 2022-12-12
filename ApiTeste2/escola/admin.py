from django.contrib import admin
from .models import Aluno

# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)