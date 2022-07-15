
from tkinter import image_names
from django.shortcuts import render,redirect
from .models import PhotoModel
import string
from random import choice
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    photos = PhotoModel.objects.all()
    paginator = Paginator(photos,9)
    page_number = request.GET.get('page')
    photosfinal = paginator.get_page(page_number)
    
    data = {'photos': photos,'photosfinal':photosfinal}
    return render(request, 'photos/index.html', data)


def new(request):
    if request.method == 'POST':
        data = request.POST
        # print('data :',data)
        chars = string.digits
        random =  ''.join(choice(chars) for _ in range(4))

        photo = PhotoModel.objects.create(
            imageid=random,
            imagename=data['imagename'],
            imageurl = data['imageurl'],
            imagedetails = data['imagedetails'],

        )
        return redirect('index')
    return render(request, 'photos/new.html')

def show(request, id):
    photo = PhotoModel.objects.get(imageid=id)
    return render(request, 'photos/show.html', {'photo': photo})


def delete(request,id):
    photo = PhotoModel.objects.get(imageid=id)
    photo.delete()
    return redirect('index')

def edit(request,id):
    photo = PhotoModel.objects.get(imageid=id)
    if request.method == 'GET':
        return render(request, 'photos/edit.html', {'photo': photo})
    if request.method == 'POST':
        data = request.POST
        photo.imagename=data['imagename']
        photo.imageurl = data['imageurl']
        photo.imagedetails = data['imagedetails']
        photo.save()
        return redirect('show',id=id)

@csrf_exempt
def photosearch(request):
    
    if request.method == 'POST':
        search = request.POST['search']
        print(search)
        photos = PhotoModel.objects.filter(imagename__icontains=search)
        return render(request,'photos/photosearch.html',{'search': search,'photos':photos})
    else:
        return render(request,'photos/photosearch.html',{})