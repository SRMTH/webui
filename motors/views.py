from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Motor

# Create your views here.


def index(request):
    ctx = {"motor_list": Motor.objects.all()}
    return render(request, "motors/index.html", ctx)


def qrcode(request, id):
    m = Motor.objects.get(pk=id)
    return HttpResponse(m.qr_code.tobytes(), content_type="image/png")
