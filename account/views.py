from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegistrationForm
from .models import Account
from .utils import SendMailNewCard

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






"""email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request,account)"""