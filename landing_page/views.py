from django.shortcuts import render
from django.http import HttpResponse

# Basic Functional View

def home(request):
    api_crud_endpoint = "<a href='http://127.0.0.1:8000/api/v1'>API</a>"
    return HttpResponse(api_crud_endpoint)