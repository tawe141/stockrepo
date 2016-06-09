from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Tag, PhotoForm, TagForm
import logging;


logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return HttpResponse("@index")


def upload(request):
    if request.method == 'GET':
        form = PhotoForm()
        return render(request, 'lumose/upload.html', {'form': form})
    elif request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.file = request.FILES['file']
            photo.save()
            return HttpResponse('received')
        else:
            return HttpResponse('error happened')