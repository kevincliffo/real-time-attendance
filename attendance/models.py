from django.db import models
from employees.models import Employee
from kiosk.models import Kiosk
from django.contrib.auth import get_user_model

User = get_user_model()

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance_records")
    kiosk = models.ForeignKey(Kiosk, on_delete=models.SET_NULL, null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(db_index=True)
    job_number_snapshot = models.CharField(max_length=20)

    class Meta:
        unique_together = ("employee", "date")
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.employee.job_number} - {self.date}"
