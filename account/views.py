from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegistrationForm,NewCardFormAdmin
from .models import Account
from .utils import SendMailNewCard
from myapp.api_wallester.wallester import createCard

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            user = Account.objects.get(email=form.cleaned_data.get('email'))
            user.username = form.cleaned_data.get('email')
            user.save()
            SendMailNewCard(user.__dict__)
            return redirect('newcard-success')
        else:
            context['registration_form'] = form
            return render(request, 'account/newcard/newcard.html', context)
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'account/newcard/newcard.html',context)


def registration_success(request):
    return render(request,'account/newcard/newcard-success.html')



def NewCardAdmin(request):
    if not request.user.is_superuser:
        return redirect('index')

    context = {}

    if request.POST:
        myform = NewCardFormAdmin(request.POST)
        if myform.is_valid():
            createCard(myform.cleaned_data)
            context['sended'] = True
        else:
            context['newcardform'] = myform
    else:
        context['newcardform'] = NewCardFormAdmin()
        context['sended'] = False

    return render(request,"account/newCardAdmin.html",context)