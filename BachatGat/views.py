from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils import custom_viewsets
from rest_framework.decorators import *


class BachatGatRegistrationViewSet(custom_viewsets.ModelViewSet):
    model = BachatGatRegistration
    queryset = BachatGatRegistration.objects.all()
    serializer_class = BachatGatRegistrationSerializers
    list_success_message = "list the data success"
    retrieve_sucess_message ="retrieve returend success"
    create_success_message = "bachatgat registration created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg":None,
        "data": None
    }
    
    @api_view(['POST'])
    def registration_form(request):
        self.response.update({
            "status": 200,
            "msg": 'employee data view featch',
            "data": {}
        })
        return Response(self.response)


class MemberRegistrationViewSet(custom_viewsets.ModelViewSet):
    model = MemberRegistration
    queryset = MemberRegistration.objects.all()
    serializer_class = MemberRegistrationSerializers
    list_success_message ="list the data "
    create_success_message = "create the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg":None,
        "data":None 
    }

    @api_view(['POST'])
    def member_registration(request):
        self.response.update({
            "status": 200,
            "msg": "member ",
            "data": {}
        })
        return response(self.response)