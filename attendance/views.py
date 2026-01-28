import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import CustomUser
from otp.services import generate_otp, verify_otp
import requests
import json

class StaffAttendanceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        employee_no = request.data.get('employee_no')
        device_id = request.data.get('device_id')

        employee_qs = CustomUser.objects.filter(employee_no=employee_no)
        created_otp = None
        if employee_qs:
            employee = employee_qs[0]
            otp = generate_otp(employee)
            created_otp = otp


            self.send_sms(employee.mobile_no, otp)
        return Response({"otp": created_otp})
    
    def send_sms(self, phone_number, otp):

        url = os.getenv("AT_API_URL")

        payload = json.dumps({
            "username": "send_sma",
            "message": f"OTP: {otp}",
            "phoneNumbers": [
                phone_number
            ]
        })
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKey': os.getenv("AT_API_KEY")
        }

        res = verify_otp(phone_number, otp)
        print("SMS RESPONSE:", res)

        response = requests.request("POST", url, headers=headers, data=payload)