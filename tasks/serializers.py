from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id','title','content', 'created', 'due_date','completed','category')





