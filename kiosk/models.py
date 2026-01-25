from django.db import models

class Kiosk(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    identifier = models.CharField(
        max_length=50,
        unique=True
    )

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
