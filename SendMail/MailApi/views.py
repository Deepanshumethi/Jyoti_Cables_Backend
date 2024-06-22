from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage


# class ContactFormView(APIView):
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         print(data)
#         subject = data.get('subject', '')
#         message = data.get('message', '')
#         email_from = data.get('email', '')
#         recipient_list = ['deepanshumethi123@gmail.com']

#         # Send email
#         send_mail(subject, message, email_from, recipient_list)

#         return Response({"success": "Email sent successfully"}, status=status.HTTP_200_OK)
    
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
            return Response({'status': 'success', 'message': 'Email sent successfully'})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})
   
