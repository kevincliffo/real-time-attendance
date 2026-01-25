from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    employee_no = serializers.CharField(
        source="employee.employee_no",
        read_only=True
    )
    verified_by = serializers.CharField(
        source="verified_by.username",
        read_only=True
    )

    class Meta:
        model = Attendance
        fields = [
            "id",
            "employee_no",
            "date",
            "timestamp",
            "verified_by",
            "kiosk",
        ]
