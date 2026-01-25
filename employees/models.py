from django.db import models
from app.models import CustomUser
from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    employee_no = models.CharField(max_length=255, unique=True)
    photo = models.FileField(upload_to="photos/", blank=True, default="")
    mobile_no = models.CharField(max_length=20, default="", verbose_name='Mobile No (+254XXXXXXXXX)', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
