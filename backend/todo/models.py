from django.db import models
from django.db.models import Q

class TodoTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class TodoTitleModel(TodoTimeModel):
    """
    If the `title` is the set, then the task belong
    to the named group `title`.
    """
    title = models.CharField(max_length=120)
    
    
    def __repr__(self):
        return "<TodoTitleModel: {}>".format(self.title)
    
    def __str__(self):
        return f"{self.title}"
    

class TodoTaskNoTitleManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(Q(title__isnull=True))

class TodoTaskTitleManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(Q(title__isnull=False))


class TodoTaskDefaultManager(models.Manager):
    pass


class TodoTaskModel(TodoTimeModel):
    """
    Task Model is hold out all the task.
    
    If `foreign key` is `null=True` then, then task belong to 
    that named group. Else the title is individual.
    """
    
    # Manager: `no_title_objects`
    # returns all the `Task` objects with `title=None`.
    no_title_objects = TodoTaskNoTitleManager()
    
    # Manager: `title_objects`
    # returns all the `Task` objects with `title` containing
    # `TodoTitleModel` instance.
    title_objects = TodoTaskTitleManager()
    
    # Default Manager
    objects = TodoTaskDefaultManager()
    
    task = models.CharField(max_length=256)
    
    # SET_NULL is required for blank=True and null=True
    title = models.ForeignKey(
        TodoTitleModel, 
        on_delete=models.SET_NULL, 
        related_name="task",
        blank=True,
        null=True
    )
    
    def __repr__(self):
        return "<TodoTaskModel: {}>".format(self.task)
    
    def __str__(self):
        return f"{self.task}"