from rest_framework import serializers

class RequestOTPSerializer(serializers.Serializer):
    employee_no = serializers.CharField(max_length=255)

class VerifyOTPSerializer(serializers.Serializer):
    employee_no = serializers.CharField(max_length=255)
    otp = serializers.CharField(max_length=6)