from django import forms
from .models import BlogPost, Message
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class BlogFormulario(forms.ModelForm):
    titulo = forms.CharField(label='Título', widget=forms.TextInput(attrs={'placeholder': 'Ingrese un Título', 'class': 'h-full-width'}), max_length=200, required=True)
    subtitulo = forms.CharField(label='Subtítulo', widget=forms.TextInput(attrs={'placeholder': 'Ingrese un Subtítulo', 'class': 'h-full-width'}), max_length=200, required=True)
    cuerpo = forms.CharField(label='Cuerpo', widget=CKEditorWidget(attrs={'placeholder': 'Ingrese el Cuerpo', 'class': 'h-full-width'},config_name='default'), required=True)
    imagen = forms.FileField(label='Imagen')

    class Meta:
        model = BlogPost
        exclude = ['autor', 'fecha']


class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label='Para', required= True)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control mb-3 h-full-width'}), label='Mensaje', required= True)

    class Meta:
        model = Message
        fields = ['recipient', 'content']