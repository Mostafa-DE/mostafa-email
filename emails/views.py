from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string


def send_email_to_client(data):
    html_body = render_to_string('customer_email.html', data)
    send_mail(
        "Hi, " + data.get('name'),
        "",
        "mostafa.de.dev@gmail.com",
        [data.get("email")],
        fail_silently=True,
        html_message=html_body,
    )


def send_email_to_me(data):
    html_body = render_to_string('mostafa_email.html', data)
    send_mail(
        f"Hi Mostafa-DE, {data.get('name')} submitted the form just now!",
        "",
        "mostafa.de.dev@gmail.com",
        ["mostafafayyado1@gmail.com"],
        fail_silently=True,
        html_message=html_body,
    )


def emailView(request):
    data = request.GET.dict()
    send_email_to_client(data)
    send_email_to_me(data)

    return JsonResponse({"message": "Email View Works!"})
