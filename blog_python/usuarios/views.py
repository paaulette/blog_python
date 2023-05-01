from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomAuthenticationForm, UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from .models import UserExtra
from django.urls import reverse_lazy

# Create your views here.
def login_request(request):
    form = CustomAuthenticationForm(request, data = request.POST)

    if request.method == "POST":
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = clave)

            if user is not None:
                login(request, user)
                
                UserExtra.objects.get_or_create(user=request.user)

                return redirect('index')
            else:
                return render(request, "login.html", {"mensaje": f"Error: el usuario y/o la contraseña son incorrectas"})
        else:
            return render(request, "login.html", {"form": form, "mensaje": f"Por favor ingresar un usuario y contraseña"})
    
    form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            usuario = form.cleaned_data["username"]

            if User.objects.filter(username=usuario).exists():
                render(request, "signup.html", {"mensaje": "Este nombre de usuario ya está en uso"})

            form.save()

            return render(request, "login.html", {"mensaje": "Usuario Creado"})
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})

@login_required
def editUser (request):
    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'profile', {"form": form})
        
    form = UserEditForm()
    return render(request, 'profile.html', {"form": form})

@login_required
def profile (request):
    if request.method == "POST":
        form = UserEditForm (request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            request.user.userextra.web = form.cleaned_data.get('web')
            request.user.userextra.descripcion = form.cleaned_data.get('descripcion')
            if form.cleaned_data.get('avatar'):
                request.user.userextra.avatar = form.cleaned_data.get('avatar')
            
            request.user.userextra.save()

            form.save()
            
            mensaje = "Se han guardado los datos correctamente"

            return render(request, "profile.html", {"form": form, "mensaje": mensaje})
        else:
            return render(request, 'profile.html', {'form': form})
        
    extra = {'avatar': request.user.userextra.avatar, 
             'web': request.user.userextra.web,
             'descripcion': request.user.userextra.descripcion,}
            
    form = UserEditForm(initial=extra, instance=request.user)

    return render(request, 'profile.html', {'form': form})

class ChangePass(PasswordChangeView):
    template_name = 'change_pass.html'
    success_url = reverse_lazy('profile')