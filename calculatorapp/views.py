from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse

# Create your views here.
def root(request): 
    return HttpResponse("root server started")

def index(request):
    return render(request,'index.html')

def submitquery(request):
    q = request.GET['query']
    try :
        ans  = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False,

        }
        return render(request,'index.html',context = mydictionary)
    except:
        mydictionary = {
            "error" : True 
        }
    return render(request,'index.html',context = mydictionary)

#404 error 
from django.conf import settings
from django.shortcuts import redirect


def error_404_view(request, exception):
    return render(request, '404.html')