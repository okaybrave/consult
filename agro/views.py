from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from agro.forms import contactform

# Create your views here.
def home(request):
    templates = 'agro/home_index.html'
    return render(request,templates)

def serv(request):
    templates = 'agro/service.html'
    return render(request,templates)

def about(request):
    templates = 'agro/about_us.html'
    return render(request,templates)    

def emailview(request):
    if request.method == 'GET':
        form = contactform()
    else:
        form = contactform(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['Email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message, email, ['admin@example'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.') 
            return redirect('success')              
    return render (request, "agro/contact_us.html",{'form':form})
def successView(request):
    return HttpResponse('success! Thank you for contacting us.')    

