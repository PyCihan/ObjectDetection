from django.shortcuts import render
from ImageServer.models import Image
from django.shortcuts import redirect
from Detector import *

# Create your views here.

def main(request):
    images = Image.objects.all()
    print(images)
    args = {'images': images}
    return render(request, 'main.html', args) #value übergibt den Parameter and die HTML-Seite und kann dort als "image" und "label" verwendet werden

def image_save(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        label = request.POST.get('titel')
        Image.objects.create(image=image, label=label)
        return redirect('main')
    return render(request, 'image_save.html')

def search(request):
    keyword = request.GET.get('keyword', '') 
    results = Image.objects.filter(label__icontains=keyword)
    return render(request, 'results.html', {'results': results})