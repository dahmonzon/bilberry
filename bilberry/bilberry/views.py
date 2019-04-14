from django.shortcuts import render
from img.models import Images

#home page controleur that display the keept images
def home(request):
    images = Images.objects.filter(verified=True,reject=False)
    #images = []
    return render(request, 'pages/home.html', {'images': images})

# handle the 404 error
def handler404(request,exception):
    return render(request, 'pages/404.html')

# handle the 500 error
def handler500(request):
    return render(request,'pages/500.html')