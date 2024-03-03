# from django.http import request
import logging
import traceback

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import ContactForm as PortfolioContactForm
from .models import Project

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


django_logger = logging.getLogger("django")


def home(request):
    context = {"projects": Project.objects.all()}

    return render(request, "portfolio/portfolio_home.html", context)


def contact(request):
    return redirect('https://www.linkedin.com/in/john-ericson-58005938/')
    # if request.method == "POST":
    #     form = PortfolioContactForm(request.POST)
    #     if form.is_valid():
    #         cleaned_data = form.cleaned_data

    #         email_sender_name = cleaned_data["email_sender_name"]
    #         email_subject = cleaned_data["email_subject"]
    #         email_sender_email = cleaned_data["email_sender_email"]
    #         email_content = cleaned_data["email_content"]

    #         flow = InstalledAppFlow.from_client_secrets_file('credentials/google_token.json', settings.GMAIL_SCOPES)
    #         creds = flow.run_local_server(port=0)

    #         service = build('gmail', 'v1', credentials=creds)
    #         message = MIMEText(f"""
    #                 sender name: <{email_sender_name}>
    #                 sender email: <{email_sender_email}>
    #                 subject: <{email_subject}>

    #                 message:
    #                 {email_content}
    #                 """)
    #         message['to'] = settings.DEFAULT_RECEIVING_EMAIL
    #         message['subject'] = f"personal website email from <{email_sender_email}>, subject<{email_subject}>"
    #         create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    #         try:
    #             message = (service.users().messages().send(userId="me", body=create_message).execute())
    #             print(F'sent message to {message} Message Id: {message["id"]}')
    #         except HTTPError as error:
    #             django_logger.error(
    #                 f"Error sending msg to email, Details:{error}\n"
    #                 + f"""
    #                 \tsender name: <{email_sender_name}>
    #                 \tsender email: <{email_sender_email}>
    #                 \tsubject: <{email_subject}>
    #                 \tmessage:<{email_content}>

    #                 Error stack <{traceback.format_exc()}>
    #                 """
    #                 + f" message was being sent to {[settings.DEFAULT_RECEIVING_EMAIL]}"
    #             )
    #             message = None

    #         # try:
    #         #     send_mail(
    #         #         subject=f"personal website email from <{email_sender_email}>, subject<{email_subject}>",
    #         #         message=f"""
    #         #         sender name: <{email_sender_name}>
    #         #         sender email: <{email_sender_email}>
    #         #         subject: <{email_subject}>

    #         #         message:
    #         #         {email_content}
    #         #         """,
    #         #         from_email=settings.EMAIL_HOST_USER,
    #         #         recipient_list=[settings.DEFAULT_RECEIVING_EMAIL],
    #         #     )
    #         # except Exception:
    #         #     django_logger.error(
    #         #         "Error sending msg to email, Details:\n"
    #         #         + f"""
    #         #         \tsender name: <{email_sender_name}>
    #         #         \tsender email: <{email_sender_email}>
    #         #         \tsubject: <{email_subject}>
    #         #         \tmessage:<{email_content}>

    #         #         Error stack <{traceback.format_exc()}>
    #         #         """
    #         #         + f" message was being sent to {[settings.DEFAULT_RECEIVING_EMAIL]}"
    #         #     )

    #         messages.success(request, "Your email has been sent.")
    #         return HttpResponseRedirect("./")

    # else:
    #     form = PortfolioContactForm()

    # return render(request, "portfolio/portfolio_contact.html", {"form": form})


def about(request):
    # posts = Post.objects.all()
    return render(request, "portfolio/portfolio_about.html", {})


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/portfolio_projects.html"
    context_object_name = "projects"
    ordering = ["-rank"]
    paginate_by = 5


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/portfolio_project.html"
