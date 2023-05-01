from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control form-control-lg'}))

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
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control mb-3 h-full-width'}), required=False)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Apellido','class': 'form-control mb-3 h-full-width'}), required=False)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control mb-3 h-full-width'}), required=False)
    descripcion = forms.CharField(max_length=500, label="", widget=forms.TextInput(attrs={'placeholder': 'Descripción','class': 'form-control mb-3 h-full-width'}), required=False)
    web = forms.CharField(max_length=500, label="", widget=forms.TextInput(attrs={'placeholder': 'Web','class': 'form-control mb-3 h-full-width'}), required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'descripcion', 'web', 'avatar']