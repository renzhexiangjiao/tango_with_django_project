from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Rango says hey there partner!</h1>
    <a href="/rango/about">About</a>
    """)

def about(request):
    return HttpResponse("""
    <h1>Rango says here is the about page.</h1>
    <a href="/rango/">Index</a>
    """)
