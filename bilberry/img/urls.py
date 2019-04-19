from django.contrib import admin
from django.urls import path
from . import views

"""
    some url path to response to all request related to  image
"""

urlpatterns = [
    path('oneItem/<int:id>',views.showOneItem, name='oneItem'), # path to display one item page
    path('treate/<str:action>/<int:id>',views.treateImage, name='treate'), #path to response treatement action
    path('upload/', views.uploadImage,name='upload'), # path to display upload new image page
    path('',views.AllImages,name='AllImages'), # path to display unchecked image
]