from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def handle_api(request):
    print(request.method)
    return HttpResponse(f"<h1>API ROUTER</h1><p>Método usado: <strong>{request.method}</strong></p>")
