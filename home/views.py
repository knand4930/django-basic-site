from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html',{'titles': 'very loving the django', 'link':'http://127.0.0.1:8000/accounts/register'})

def expression(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    r=a+2*b
    return render(request, 'output.html', {'result': r})