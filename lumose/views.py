from django.shortcuts import render
from django.http import HttpResponse
import logging;


logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return HttpResponse("@index")


def upload(request):
    if request.method == 'GET':
        return render(request, 'lumose/upload.html')
    elif request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        return HttpResponse('received')