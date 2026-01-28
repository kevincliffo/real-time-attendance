import hashlib
import secrets
from datetime import timedelta
from django.utils import timezone
from .models import OTP

def generate_otp(employee):
    raw_otp = f"{secrets.randbelow(1000000):06d}"

    otp_hash = hashlib.sha256(raw_otp.encode()).hexdigest()

    otp = OTP.objects.create(
        user=employee,
        otp_hash=otp_hash,
        expires_at=timezone.now() + timedelta(minutes=3)
    )

    return raw_otp

def verify_otp(employee, submitted_otp):
    otp_hash = hashlib.sha256(submitted_otp.encode()).hexdigest()

    try:
        otp = OTP.objects.get(
            user=employee,
            otp_hash=otp_hash,
            is_used=False,
            expires_at__gt=timezone.now()
        )
    except OTP.DoesNotExist:
        return False

    otp.is_used = True
    otp.save(update_fields=["is_used"])

    return True
