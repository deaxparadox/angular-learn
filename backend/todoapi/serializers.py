from rest_framework import serializers

from todo.models import TodoTitleModel, TodoTaskModel


    



class TodoTaskSerializer(serializers.ModelSerializer):
    """
    Serilize all the task object, both with `title` and with `no title`
    """
    
    title = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)
    
    class Meta:
        model = TodoTaskModel
        fields = ['task', 'title']
        
        


class TodoTaskNoTitleSerializer(serializers.ModelSerializer):
    """
    Serilize tasks with `no title` only
    """
    
    class Meta:
        model = TodoTaskModel
        fields = ['task']


class TodoTitleSerializer(serializers.ModelSerializer):
    """
    Serialize title
    """
    class Meta:
        model = TodoTitleModel
        fields = ['title']



# Serilizer for title or group 
# with their task
class TodoTitleWithTasksSerializer(serializers.Serializer):
    """
    Serilizers all title objects,
    with their tasks
    """
    
    title = serializers.CharField()
    task = TodoTaskNoTitleSerializer(many=True)
    