from django.shortcuts import render
from.models import ContactUs
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.


def home(request):
    context = {
        
    }
    return render(request,'home.html',context)


def about(request):
    context = {
        
    }
    return render(request,'about.html',context)


def project(request):
    
    projects_show = [
        {
            'title' : 'Rasoi Connect',
            'path' : 'images/rasoi_connect.PNG',
         },
        
        {
            'title' : 'Ecommerce',
            'path' : 'images/ecommerce.PNG',
         },
        
        {   'title' : 'Timtable Scheduler',
            'path' : 'images/timtable.PNG',
         },
        
        {   'title' : 'CRUD',
            'path' : 'images/CRUD.PNG',
         },
        
        {   'title' : 'photo Uploader',
            'path' : 'images/photo_uploader.PNG',
         },
        
        {   'title' : 'To Do List',
            'path' : 'images/todolist.PNG',
         },
        
        {   'title' : 'Portfolio',
            'path' : 'images/portfolio.PNG',
         },
        
        {   'title' : 'Labour Hiring',
            'path' : 'images/labour_hiring.PNG',
         },
    ]
    return render(request,'project.html', {'projects_show' : projects_show})



def experience(request):
    experience = [
        {
            'company' : 'ABC',
            'position' : 'Website Designer',
         },
    
        {
            'company' : 'ABC-2',
            'position' : 'Website Developer',
         },
        
        {
            'company' : 'ABC-3',
            'position' : 'Python Developer',
         },
        
        {
            'company' : 'ABC-4',
            'position' : 'Django Developer',
         },
    ]
    return render(request,'experience.html',{'experience' : experience})

def certification(request):
    context = {
        
    }
    return render(request,'certification.html',context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
       
        contact_data = ContactUs(name=name,phone=phone,email=email,message=message)
        contact_data.save()
    
      
    context = {   
    }
    return render(request,'contact.html',context)



def resume(request):
    resume_path = "myresume/Bithi Mondal Curriculum Vitae.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(),content_type = "application/pdf")
            response['Content-Disposition'] = 'attachment'; filename = "Bithi Mondal Curriculum Vitae.pdf"
            return response
        
    else:
        return HttpResponse("Resume not Found", status = 404)
    
    context = {     
    }
    return render(request,'resume.html',context)

