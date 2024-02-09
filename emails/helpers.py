from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_email_to_client(data):
    html_body = render_to_string('customer_email.html', data)
    send_mail(
        "Hi, " + data.get('name'),
        "",
        settings.EMAIL_HOST_USER,
        [data.get("email")],
        fail_silently=True,
        html_message=html_body,
    )


def send_email_to_me(data):
    html_body = render_to_string('mostafa_email.html', data)
    send_mail(
        f"Hi Mostafa-DE, {data.get('name')} submitted the form just now!",
        "",
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_SEND_USER],
        fail_silently=True,
        html_message=html_body,
    )