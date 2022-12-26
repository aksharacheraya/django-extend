from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def classes(request):
    return render(request,'classes.html')
def contact(request):
    return render(request,'contact.html')
def shortcodes(request):
    return render(request,'shortcodes.html')
def shows(request):
    return render(request,'shows.html')
def test(request):
    return render(request,'test.html')

