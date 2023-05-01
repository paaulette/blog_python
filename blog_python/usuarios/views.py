from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from usuarios.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    form = CustomAuthenticationForm(request, data = request.POST)

    if request.method == "POST":
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(request, username=usuario, password=clave)

            if user is not None:
                login(request, user)

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

            return render(request, "/login.html", {"mensaje": "Usuario Creado"})
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

# @login_required
# def profile (request):
#     if request.method == "POST":
#         form = AvatarForm (request.POST, request.FILES)

#         if form.is_valid():
#             user = User.objects.get(username=request.user.username)

#             avatar = AvatarForm (user = user, imagen = form.cleaned_data.get['imagen'])
#             avatar.save()

#             return render(request, "/index")
#     else:
#         form = AvatarForm()

#     return render(request, "profile", {"form": form})