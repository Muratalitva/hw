from django.shortcuts import render,redirect
from django.core.mail import send_mail
from settings.models import Settings
# # Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    return render(request, "index.html", locals())