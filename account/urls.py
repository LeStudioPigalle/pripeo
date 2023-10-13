from django.urls import path,include
from account.views import registration_view,registration_success,login
from . import views

urlpatterns = [
    path('',views.registration_view,name='newcard'),
    path('success',views.registration_success,name='newcard-success'),
    path('ordernewcard',views.NewCardAdmin,name='newcardwallester'),
]