from django.urls import path


from .view import root_view

app_name = "todoapi"

urlpatterns = [
    path("", root_view, name='root_view'),
    path("task/", root_view, name='root_view'),
]
