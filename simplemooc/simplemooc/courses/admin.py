from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    # Customização do formulario/listagem dos dados no Admin
    list_display = ['name', 'slug', 'start_date', 'created_at']  # nome dos campos da tabela
    search_fields = ['name', 'slug']  # campos para pesquisa
    prepopulated_fields = {'slug': ('name',)}  # gerando o campo slug de forma automatica a partir do nome

admin.site.register(Course, CourseAdmin)
