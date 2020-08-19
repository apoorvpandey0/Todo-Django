from django.shortcuts import render,redirect
from .forms import *
from .models import Task
# Create your views here.

def home_view(request):
    if request.method == 'POST':
        form=Task_Form(request.POST)
        if form.is_valid() :
            Title=form.cleaned_data.get('title')
            # messages.success(request,f"New task added Title:{Title}!")
            form.save()
            return redirect('home')
    else :
        form=Task_Form()
    context={
        "form":form,
        'tasks':Task.objects.all(),
        "title":"Home"
    }

    return render(request,'pages/home.html',context)
