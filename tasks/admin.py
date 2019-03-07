from django.contrib import admin
from .models import *

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("created_by","title","completed" ,"created", "due_date","category")



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)



admin.site.register(TodoList, TodoListAdmin)

admin.site.register(Category, CategoryAdmin)



