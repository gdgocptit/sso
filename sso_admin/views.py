from django.shortcuts import render

# Create your views here.

from django.http import *

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "sso_admin/index.html")
