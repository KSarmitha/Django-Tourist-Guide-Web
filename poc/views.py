from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'home.html', {'name': 'John Doe'})

def add(request):
    # for get method
    # val1 = request.GET['num1']
    # val2 = request.GET['num2']
    # For post method
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html', {'result': res})