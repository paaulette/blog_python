from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_images/', null= False, blank=False)

    def __str__(self):
        return self.titulo

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De: {self.sender.username}, Para: {self.recipient.username}, Mensaje: {self.content}"