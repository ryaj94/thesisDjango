from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, student_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from joblib import load
model = load('./../saveModels/regressor.joblib')



from .models import *
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='loginPage')
@student_only
def home(request):
    userprof = request.user.studentprof
    print(userprof)

    context = {'userprof': userprof}
    return render(request, 'accounts/StudentProfile.html' , context)

@login_required(login_url='loginPage')
@student_only
def studadvise(request):
    usergrade = request.user.studentgrades
    userprof1 = request.user.studentprof
   
    
    arr=[[311,usergrade.gned02], [312,usergrade.gned05], [313,usergrade.gned11], [314,usergrade.cosc50], [315,usergrade.dcit21], [316,usergrade.dcit22], [317,usergrade.fitt1]]    
    rows, cols = (7, 2)

    subj=[]
    for f in range(rows):
        subj.append(model.predict([arr[f]]))

    print(subj)

    context = {'usergrade': usergrade, 'userprof': userprof1, 'subj':subj }
    return render(request, 'accounts/student advising.html', context )


@unauthenticated_user
def registeruser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.group.add(group)
            studentprof.objects.create(
                user=user
            )
            messages.success(request, "Account successfuly created for "+ username)
            return redirect("home")

    context = {'form': form}
    return render(request, 'accounts/regform.html', context)



@unauthenticated_user
def loginPage(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')

     context = {}
     return render(request, 'accounts/index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def sampleInput(request):
    return render(request, 'accounts/sampleInput.html')

def predict(request):
    rows, cols = (7, 2)
   
    subj=[]
    arr=[]
    for f in range(rows):
        
        subj.append(model.predict([arr[f]]))
        
    print(subj)

    return render(request, 'accounts/sampleOutput.html', {'result': subj})



#@login_required(login_url='loginPage')
#def adminPage(request):
#    return render(request, 'http://127.0.0.1:8000/admin/')    

#def loginstud(request, pk_test):
 #   studentprof1 = studentprof.objects.get(user_id=pk_test)
  #  context = {'studentprof':studentprof1, }
   # return render(request, 'accounts/StudentProfile.html', context)