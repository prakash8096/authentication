from django.shortcuts import render,redirect
from .forms import Extra
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method=='POST':
        form=Extra(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form=Extra()
    form=Extra()
    

    
    return render(request,'signup.html',{'form':form})

def home(request):
    return render(request,'home.html')
