from rest_framework import serializers

from todo.models import TodoTitleModel, TodoTaskModel

class TodoTitleSeralizer(serializers.ModelSerializer):
    class Meta:
        model = TodoTitleModel
        fields = ['title']
        
class TodoTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TodoTaskModel
        fields = ['task', 'title']