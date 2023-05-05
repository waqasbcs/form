from django.shortcuts import render
from .forms import studentregistration
from.models import user

# Create your views here.
def showformdata(request):

    if request.method == 'POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            fim=fm.cleaned_data['first_name']
            lim=fm.cleaned_data['last_name']
            em=fm.cleaned_data['email']
            pa=fm.cleaned_data['password']
            reg=user(id=1,first_name=fim,last_name=lim,email=em,password=pa)
            reg.save()
    else:
        fm= studentregistration()
    return render(request, 'enroll/userregistration.html',{'form':fm})
