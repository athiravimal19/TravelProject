from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
    return render(request,"index.html")

# def operations(request):
#     num1 = int(request.GET['n1'])
#     num2 = int(request.GET['n2'])
#     res=num1+num2
#     s=num1-num2
#     m = num1*num2
#     q=num1/num2
#     return render(request,"result.html",{'r':res,'su':s,'mu':m,'di':q})
