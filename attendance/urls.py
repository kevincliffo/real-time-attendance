from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'attendance'

urlpatterns = [
    path('staff-attendance/', views.StaffAttendanceView.as_view(), name="staff-attendance"),
]