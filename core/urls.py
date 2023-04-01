from django.contrib import admin
from django.urls import path

from emails.views import emailView, homeView

urlpatterns = [
    path('', homeView, name="email"),
    path('admin/', admin.site.urls),
    path('email/', emailView, name="email"),
]
