from django.contrib import admin
from main.models import Produto
from main.models import Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
