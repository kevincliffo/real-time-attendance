from django.db import models
from app.models import CustomUser

class OTP(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="otps"
    )

    otp_hash = models.CharField(max_length=128)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.employee_no}"

