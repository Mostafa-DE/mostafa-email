from django.contrib import admin
from django.urls import path
from emails.views import email, home


urlpatterns = [
    path('', home, name="home"),
    path('email/', email, name="email"),
    path('admin/', admin.site.urls),
]
