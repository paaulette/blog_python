from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth import authenticate

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    #username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control form-control-lg'}))
    #password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control form-control-lg'}))

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control form-control-lg'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Usuario','class': 'form-control mb-3'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control mb-3'}))
    password1 = forms.CharField(label = "", widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña','class': 'form-control mb-3'}))
    password2 = forms.CharField(label = "", widget = forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña','class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k: "" for k in fields}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
 
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control mb-3 h-full-width'}))
    descripcion = forms.CharField(max_length=500, label="", widget=forms.EmailInput(attrs={'placeholder': 'Descripción','class': 'form-control mb-3 h-full-width'}))
    web = forms.CharField(max_length=500, label="", widget=forms.EmailInput(attrs={'placeholder': 'Web','class': 'form-control mb-3 h-full-width'}))
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'descripcion', 'web', 'avatar']