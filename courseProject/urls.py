from django.urls import path
from . import views

urlpatterns = [
    path("", views.students, name = 'students'),
    path("student/results", views.results)
]
