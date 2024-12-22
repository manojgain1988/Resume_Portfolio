from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=50,blank=True, null=True)
    message = models.CharField(max_length=500,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def ImageUrl(self):
            if self.image:
                
                return self.image.url
            else:
                return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    
    
    def __str__(self):
        return self.name
    