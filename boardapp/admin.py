from django.contrib import admin
from .models import BoardModel, TodoModel

# Register your models here.
admin.site.register(BoardModel)
admin.site.register(TodoModel)
