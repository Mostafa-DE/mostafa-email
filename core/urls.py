from django.contrib import admin
from django.urls import path

from emails.views import emailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', emailView, name="email"),
]
