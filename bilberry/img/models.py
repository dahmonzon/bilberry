from django.db import models

"""
name : field that represente the name give to the images
created : field that represente the image create date
reject : field that represente the reject status by default false
verified : field that represente the verified status by default false
images : field that represente the image path on the project folder location

"""
class Images(models.Model):
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    reject = models.BooleanField()
    verified = models.BooleanField()
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name