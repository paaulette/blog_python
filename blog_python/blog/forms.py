from django import forms
from django.contrib.auth import get_user_model
from .views import BlogPost

User = get_user_model()

class BlogFormulario(forms.ModelForm):
    titulo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Título', 'class': 'h-full-width h-remove-bottom'}), max_length=200, required=True)
    subtitulo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Subtítulo', 'class': 'h-full-width h-remove-bottom'}), max_length=200, required=True)
    cuerpo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cuerpo', 'class': 'h-full-width'}), max_length=200, required=True)
    imagen = forms.FileField(label='Imagen')
    autor = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        exclude = ['fecha']
