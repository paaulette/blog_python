from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from usuarios.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('change-pass/', views.ChangePass.as_view(), name='change_pass'),
]