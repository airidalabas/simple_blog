from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('registration/', views.UserRegisterView.as_view(), name="registration"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit_profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html")),
    path('password/', views.PasswordsChangeView.as_view(template_name="registration/change_password.html")),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name="show_profile_page"),
    ]
