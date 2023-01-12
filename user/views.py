from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
# Create your views here.


@login_required
def update_user(request,pk):
    #form=NewUserForm(request.POST,instance=request.user)
    #either adding this line and instance=user or the way you see it now
    #user=NewUser.objects.get(pk=pk)
    if request.method == 'POST':
        form=NewUserForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()

        return redirect("/admin")
        
    else:
         form=NewUserForm(instance=request.user)
    return render(request,'input.html',{"form":form})

