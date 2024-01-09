from . import views
from django.urls import path
urlpatterns = [
    path("employee/create", views.CreateEmployee.as_view()),
    path("employee/update", views.UpdateEmployee.as_view()),
    path("employee/login", views.EmployeeLogin.as_view()),
]