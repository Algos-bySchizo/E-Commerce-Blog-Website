from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')
def about(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at about')
def contact(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at contact us')
def tracker(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at tracker')
def search(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at search')
def prodview(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at product view page')
def checkout(request):
    # return render(request,'shop/index.html')
    return HttpResponse('we\'re at checkout page')