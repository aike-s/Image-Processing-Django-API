from django.urls import path
from .views import JobView

urlpatterns = [
    path('job/<int:id>', JobView.as_view(), name='job_status')
]