from django.urls import path
from .views import home, delete_task, done_task

urlpatterns = [
    path("", home, name="home"),
    path("delete/<int:id>",delete_task, name="delete"),
    path("done/<int:id>",done_task, name="done")
]