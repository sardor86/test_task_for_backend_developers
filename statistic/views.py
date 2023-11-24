from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Employee, Order


class EmployeeApiView(APIView):
    def get(self, request, employee_id: int) -> Response:
        if not ('year' in request.query_params and 'month' in request.query_params):
            return Response('Неправильный запрос', status=status.HTTP_400_BAD_REQUEST)

        employee_data = Employee.objects.filter(id=employee_id).first()

        if employee_data is None:
            return Response('Нет такого сотрудника', status.HTTP_404_NOT_FOUND)

        data_list = Order.objects.select_related('product').filter(date__year=request.query_params['year'],
                                                                   date__month=request.query_params['month'],
                                                                   employee_id=employee_id)
        return Response({
            'fullname': employee_data.fullname,
            'client_quantity': data_list.distinct('client_id').count(),
            'product_quantity': data_list.count(),
            'total_price': sum([data.product.price for data in data_list])
        })


class EmployeeStatisticApiView(APIView):
    def get(self, request):
        if not ('year' in request.query_params and 'month' in request.query_params):
            return Response('Неправильный запрос', status=status.HTTP_400_BAD_REQUEST)

        data_list = Order.objects.select_related('product',
                                                 'employee').filter(date__year=request.query_params['year'],
                                                                    date__month=request.query_params['month'])

        return Response({
            'data':
            [{
                'id': data.employee_id,
                'fullname': data.employee.fullname,
                'client_quantity': data_list.filter(employee_id=data.employee_id).distinct('client_id').count(),
                'product_quantity': data_list.filter(employee_id=data.employee_id).count(),
                'total_price': sum([d.product.price for d in data_list.filter(employee_id=data.employee.id)])
            } for data in data_list.distinct('employee_id')]
        })


class ClientStatisticApiView(APIView):
    def get(self, request, client_id: int):
        if not ('year' in request.query_params and 'month' in request.query_params):
            return Response('Неправильный запрос', status=status.HTTP_400_BAD_REQUEST)

        client_data = Client.objects.filter(id=client_id).first()

        if client_data is None:
            return Response('Нет такого клиента', status.HTTP_404_NOT_FOUND)

        data_list = Order.objects.select_related('product').filter(client_id=client_id,
                                                                   date__year=request.query_params['year'],
                                                                   date__month=request.query_params['month'])

        return Response({
            'client_id': client_id,
            'fullname': client_data.fulname,
            'product_quantity': data_list.count(),
            'total_price': sum([data.product.price for data in data_list])
        })
