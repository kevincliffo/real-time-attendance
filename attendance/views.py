import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import CustomUser
from otp.services import generate_otp, verify_otp

class StaffAttendanceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        employee_no = request.data.get('employee_no')
        device_id = request.data.get('device_id')

        employee = CustomUser.objects.filter(employee_no=employee_no)
        created_otp = None
        if employee:
            otp = generate_otp(employee[0])
            created_otp = otp

        return Response({"otp": created_otp})