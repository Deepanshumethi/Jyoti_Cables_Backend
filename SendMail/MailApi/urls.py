from django.urls import path
from .views import SendEmailAPIView, home

urlpatterns = [
    path('send-email/', SendEmailAPIView.as_view(), name='send_email'),
    path('', home, name='home'),
]
