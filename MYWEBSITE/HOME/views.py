from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request, 'HOME/Home Page.html')

def about(request):
    return render(request, 'HOME/About Page.html')

