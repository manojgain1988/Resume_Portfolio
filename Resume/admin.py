from django.contrib import admin
from.models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','image_tag','created_at','updated_at']
admin.site.register(ContactUs,ContactUsAdmin)