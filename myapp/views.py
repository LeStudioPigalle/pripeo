from datetime import datetime

from django.shortcuts import render, redirect,HttpResponse
from account.models import Account
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from account.forms import AccountAuthenticationForm,PasswordUpdateForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

#API
from .api_wallester import wallester
import json
import csv



def tables_test(request):
    context = {}
    context['patients'] = [["<a href='https://facebook.com'>01</a>" , "Johnathan" , "<a href='https://facebook.com'> <button type='button' class='btn btn-primary waves-effect waves-light'>Primary</button></a>" , "Senior Implementation Architect" , "Hauck Inc" , "Holy See"] , ["02" , "Harold" , "harold@example.com" , "Forward Creative Coordinator" , "Metz Inc" , "Iran"] , ["03" , "Shannon" , "shannon@example.com" , "Legacy Functionality Associate" , "Zemlak Group" , "South Georgia"] , ["04" , "Robert" , "robert@example.com" , "Product Accounts Technician" , "Hoeger" , "San Marino"] , ["05" , "Noel" , "noel@example.com" , "Customer Data Director" , "Howell - Rippin" , "Germany"] , ["06" , "Traci" , "traci@example.com" , "Corporate Identity Director" , "Koelpin - Goldner" , "Vanuatu"] , ["07" , "Kerry" , "kerry@example.com" , "Lead Applications Associate" , "Feeney, Langworth and Tremblay" , "Niger"] , ["08" , "Patsy" , "patsy@example.com" , "Dynamic Assurance Director" , "Streich Group" , "Niue"] , ["09" , "Cathy" , "cathy@example.com" , "Customer Data Director" , "Ebert, Schamberger and Johnston" , "Mexico"] , ["10" , "Tyrone" , "tyrone@example.com" , "Senior Response Liaison" , "Raynor, Rolfson and Daugherty" , "Qatar"]]
    return render(request,'myapp/tables-gridjs.html',context)

# Create your views here.

def block_card(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    myuser = Account.objects.get(id=request.user.id)
    data_card = wallester.getCardsByIdAccount(myuser.id_compte_wallester)

    # Blocage Carte :
    test_blocage = wallester.blockCard(data_card['id'])

    return redirect('index')

def unblock_card(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    myuser = Account.objects.get(id=request.user.id)
    data_card = wallester.getCardsByIdAccount(myuser.id_compte_wallester)

    # Blocage Carte :
    test_blocage = wallester.unblockCard(data_card['id'])

    return redirect('index')

def download_hist(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    myuser = Account.objects.get(id=request.user.id)
    data_card = wallester.getCardsByIdAccount(myuser.id_compte_wallester)

    link_card_history = wallester.getCardHistory_dl(data_card['id'],1000)

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="historique-carte-pripeo.csv"'},
    )

    writer = csv.writer(response)

    for elem in link_card_history:
        writer.writerow(elem)

    return  response


def index(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    #requetes API :
    myuser = Account.objects.get(id=request.user.id)
    #print(datetime.now())
    data_card = wallester.getCardsByIdAccount(myuser.id_compte_wallester)
    if data_card is None:
        return redirect('logout')
    #print(datetime.now())
    data_account = wallester.getAccountById(myuser.id_compte_wallester)

    try:
        data_card_history = wallester.getCardHistory(myuser.id_compte_wallester,100)
    except:
        data_card_history = {}

    context = {}
    context['user'] = myuser
    context['card'] = data_card
    try:
        context['card_account'] = str(data_account['account']['balance'])+" "+str(data_account['account']['currency_code'])
    except : pass
    context['card_history'] = data_card_history

    return render(request,'myapp/pages-starter.html',context)

def infos(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('infos')
        else:
            context['password_form'] = form
            return render(request, 'myapp/infos.html', context)

    form = PasswordChangeForm(request.user)
    context['password_form'] = form
    context['user'] = Account.objects.get(id=request.user.id)

    return render(request, 'myapp/infos.html', context)

"""def infos(request):
    user_auth = request.user

    if not user_auth.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = PasswordUpdateForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('infos')
        else:
            context['password_form'] = form
            return render(request, 'myapp/infos.html', context)

    form = PasswordUpdateForm(request.user)
    context['password_form'] = form
    context['user'] = Account.objects.get(id=request.user.id)

    return render(request, 'myapp/infos.html', context)"""

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email,password=password)

            if user :
                login(request,user)
                return redirect('index')
        else:
            context['login_form'] = form
            #print(context)
            return render(request, 'myapp/login.html', context)

    else :
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request,'myapp/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')

