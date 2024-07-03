from typing import Optional

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from todo.models import TodoTitleModel, TodoTaskModel
from ..serializers import TodoTaskSerializer, TodoTaskNoTitleSerializer, TodoTitleWithTasksSerializer

@api_view(['GET'])
def root_view(request):
    return Response({
        "message": "Welcome to To-do Full stack Application."
    }, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def task_view(request):
    
    # `title` key word is required in query,
    # for get the tasks related to that title or group
    title_key = request.GET.get("title")
    
    if title_key:
        
        # if title or group name is given,
        # return tasks related to this title.
        # 
        
        group = TodoTitleModel.objects.get(title=title_key)
        tasks = group.task(manager="objects").all()
        res = dict(
            title = group.title,
            task = tasks
        )
        serializer = TodoTitleWithTasksSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        
        # if title is not, given simply return all the tasks.
        # 
        tasks: Optional[TodoTaskModel] = TodoTaskModel.objects.all()
        serializer: Optional[TodoTaskSerializer] = TodoTaskSerializer(tasks, many=True)
    
    
    
    return Response({
        "task": serializer.data
    }, status=status.HTTP_200_OK)