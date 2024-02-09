from django.http import JsonResponse
from django.shortcuts import redirect
from .helpers import send_email_to_client, send_email_to_me


def email(request):
    data = request.GET.dict()
    send_email_to_client(data)
    send_email_to_me(data)

    return JsonResponse({})


def home(request):
    return redirect("https://mostafade.com")
