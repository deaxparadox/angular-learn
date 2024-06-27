from typing import Optional

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from todo.models import TodoTitleModel, TodoTaskModel
from ..serializers import TodoTaskSerializer, TodoTitleSeralizer

@api_view(['GET'])
def root_view(request):
    return Response({
        "message": "Welcome to To-do Full stack Application."
    }, status=status.HTTP_200_OK)
    

@api_view(['GET', "POST"])
def task_view(request):
    title = request.GET.get("tilte")
    tasks: Optional[TodoTaskModel] = None
    
    if title:
        tasks = TodoTaskModel.title_objects.all()
    else:
        tasks = TodoTaskModel.no_title_objects.all()
        
    serializer = TodoTaskSerializer(tasks, many=True)
    
    Response({
        "tasks": tasks
    }, status=status.HTTP_200_OK)