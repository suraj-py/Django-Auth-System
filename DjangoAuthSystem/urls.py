
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from User import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='logout'),
    path('password_reset/',
             auth_views.PasswordResetView.as_view(template_name='User/password_reset.html'),
             name='password_reset'),

    path('password_reset/done/',
             auth_views.PasswordResetDoneView.as_view(template_name='User/password_reset_done.html'),
             name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(template_name='User/password_reset_confirm.html'),
             name='password_reset_confirm'),

    path('password_reset_complete/',
             auth_views.PasswordResetCompleteView.as_view(template_name='User/password_reset_complete.html'),
             name='password_reset_complete'),
]

