from . import views
from django.urls import path
urlpatterns = [
    path("employee/create", views.CreateEmployee.as_view()),
]