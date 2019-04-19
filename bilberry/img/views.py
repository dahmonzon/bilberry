from django.shortcuts import render
from img.models import Images
from django.http import Http404 ,HttpResponse ,HttpResponseNotFound

# unchecked image controleur for displaying all unchecked images
def AllImages(request):
    try:
        images = Images.objects.all()
    except:
        images = None
    return render(request, 'pages/all.html',{'images': images})

# upload image controleur for handle form request of upload  
def uploadImage(request):
    if request.method == 'POST':
        image = Images()
        image.name = request.POST.get('nom')
        image.images = request.FILES.get('images')
        image.reject = False
        image.verified = False
        image.save()
        success = 'Your image was successful upload '
        return render(request,'pages/upload.html',{"success": success})
    else :
        success = None
        return render(request, 'pages/upload.html',{"success": success})

# controleur to display one images per pages
def showOneItem(request,id):
    try:
        image = Images.objects.get(pk=id)
    except:
        raise Http404()
    return render(request, 'pages/oneitem.html',{'image': image})

# controleur for handle reject or keept querry 
def treateImage(request,action,id):
    img = Images.objects.get(pk=id)
    # if img.verified == True:
    #     return render(request, 'pages/all.html')
    if action == 'reject': # by default keept
        img.reject = True 
    img.verified = True
    img.save()
    return HttpResponse()
    # try:
    #    image = Images.objects.filter(verified=False)
    #    if len(image) == 0:
    #        image = None
    #        return render(request, 'pages/oneItem.html', {'image': image})
    # except :
    #     image = None
    #     return render(request, 'pages/oneItem.html', {'image': image})
    # return render(request, 'pages/oneItem.html',{'image':image[0]})