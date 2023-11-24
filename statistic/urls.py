from django.urls import path
from .views import EmployeeApiView, EmployeeStatisticApiView, ClientStatisticApiView

urlpatterns = [
    path('statistics/employee/<int:employee_id>/', EmployeeApiView.as_view()),
    path('statistics/client/<int:client_id>/', ClientStatisticApiView.as_view()),
    path('employee/statistics/', EmployeeStatisticApiView.as_view()),
]
