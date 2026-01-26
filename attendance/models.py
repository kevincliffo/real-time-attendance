from django.db import models
from app.models import CustomUser
from kiosk.models import Kiosk
from django.contrib.auth import get_user_model

User = get_user_model()

class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="attendance_records")
    kiosk = models.ForeignKey(Kiosk, on_delete=models.SET_NULL, null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(db_index=True)
    job_number_snapshot = models.CharField(max_length=20)

    class Meta:
        unique_together = ("user", "date")
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.user.employee_no} - {self.date}"
