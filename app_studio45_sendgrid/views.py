from django.shortcuts import render
from django.http import HttpResponse
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


def sendgrid_view_data(request):
    sg = sendgrid.SendGridAPIClient(api_key='Enter Your Key Here')
    from_email = Email("Enter Your Sendgrid Email Address Here")
    to_email = To("Enter Your Email Here")
    subject = "Studio45creations Email Sending"
    content = Content("text/plain", "this is studio45creations email sending process")
    mail = Mail(from_email, to_email, subject, content)
    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    if response.status_code == 202:
        return HttpResponse('Email send Successfully.')
    else:
        return HttpResponse('error sending a email from user')

# Create your views here.
