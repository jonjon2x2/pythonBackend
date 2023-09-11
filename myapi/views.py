import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework import permissions
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .serializers import CustomerSerializer
from .models import Customer

class CustomerApiView(generics.GenericAPIView):
    # add permission to check if user is authenticated
    permission_classes = (IsAuthenticated,)

    # Get all Customers
    def get(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create Customer
    def post(self, request):
        number = request.data.get('phone_no')
        email = request.data.get('email')

        # Validate Phone Number
        if not Utilities.isPhoneNumberValid(number):
            return Response({"status": "fail", "message": f"Phone number is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate Email
        if validate_email(email):   
            return Response({"status": "fail", "message": f"Email format is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get(email),
            'phone_no': request.data.get(number),
            'address': request.data.get('address'),
            'postcode': request.data.get('postcode'),
            'state': request.data.get('state')
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerApiDetailView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_Customer(self, id):
        try:
            return Customer.objects.get(id=id)
        except:
            return None

    # Get Specific Customer
    def get(self, request, id):
        Customer = self.get_Customer(id=id)
        if Customer == None:
            return Response({"status": "fail", "message": f"Customer with Id: {id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(Customer)
        return Response({"status": "success", "data": {"Customer": serializer.data}})

    # Update Specific Customer
    def put(self, request, id):
        Customer = self.get_Customer(id)
        number = request.data.get('phone_no')
        email = request.data.get('email')

        if Customer == None:
            return Response({"status": "fail", "message": f"Customer with Id: {id} not found"}, status=status.HTTP_404_NOT_FOUND)

        # Validate Phone Number
        if not Utilities.isPhoneNumberValid(number):
            return Response({"status": "fail", "message": f"Phone number is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate Email
        try:
            validate_email(email)
        except ValidationError:
            return Response({"status": "fail", "message": f"Email format is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(Customer, data=request.data, partial=True)
        if serializer.is_valid():
            return Response({"status": "success", "message": f"Customer with Id: {id} updated successfully"})
    
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Specific Customer
    def delete(self, request, id):
        Customer = self.get_Customer(id)
        if Customer == None:
            return Response({"status": "fail", "message": f"Customer with Id: {id} not found"}, status=status.HTTP_404_NOT_FOUND)

        Customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Utilities():
    def isPhoneNumberValid(number):
        pattern = re.compile("^(\+?6?01)[02-46-9]-*[0-9]{7}$|^(\+?6?01)[1]-*[0-9]{8}$")
        return pattern.match(number)