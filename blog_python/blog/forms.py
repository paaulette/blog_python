from django import forms
from .views import BlogPost

class BlogFormulario(forms.ModelForm):
    titulo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Título', 'class': 'h-full-width h-remove-bottom'}), max_length=200, required=True)
    subtitulo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Subtítulo', 'class': 'h-full-width h-remove-bottom'}), max_length=200, required=True)
    cuerpo = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Cuerpo', 'class': 'h-full-width'}), required=True)
    imagen = forms.FileField(label='Imagen')

    class Meta:
        model = BlogPost
        exclude = ['autor', 'fecha']

