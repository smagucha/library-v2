"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraryv2.urls')),
    path('accounts/', include("accounts.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset_form.html"),
     name ='reset_password'),
    path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name ='accounts/password_reset_confirm.html'),),
    path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),),

]
