from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('infos/',views.infos,name='infos'),

    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='myapp/password_reset.html'),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'),
         name='password_reset_complete'),

    path('table/',views.tables_test,name='table'),


    path('block-card/',views.block_card,name='block-card'),
    path('unblock-card/',views.unblock_card,name='unblock-card'),
    path('hist/',views.download_hist,name='hist'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
