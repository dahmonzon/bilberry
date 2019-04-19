from django.shortcuts import render
from img.models import Images

#home page controleur that display the keept images
def home(request):
    keeptimages = Images.objects.filter(verified=True,reject=False)
    rejectimages = Images.objects.filter(verified=True,reject=True)
    images = Images.objects.all()
    uncheckedImages = len(images) - (len(keeptimages)+len(rejectimages)) 
    #images = []
    return render(request, 'pages/home.html', {'KeeptImages': len(keeptimages),'rejectImages': len(rejectimages),'allImages': len(images),'uncheckedImages': uncheckedImages})

# handle the 404 error
def handler404(request,exception):
    return render(request, 'pages/404.html')

# handle the 500 error
def handler500(request):
    return render(request,'pages/500.html')