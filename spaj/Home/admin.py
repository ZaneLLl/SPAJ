from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado','alterado', 'status')
    list_filter = ('status', 'publicado', 'criado', 'autor')
    date_hierarchy = 'publicado'
    raw_id_fields = ('autor',)
    search_fields = ('titulo', 'conteudo', 'status')
    prepopulated_fields = {'slug':('titulo',)}
