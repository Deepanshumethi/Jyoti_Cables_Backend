from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

class SendEmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject', '')
        message = request.data.get('message', '')
        from_email = request.data.get('from_email', '')
        recipient_list = request.data.get('recipient_list', [])

        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=recipient_list
            )
            email.content_subtype = "html"  # Specify the content type as HTML
            email.send()
            return Response({'status': 'success', 'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def home(request):
    content = """<div>
    <h2>Stanley cables backend</h2>
    </div>"""
    return HttpResponse(content)
