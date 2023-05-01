from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from blog.models import BlogPost
from .forms import BlogFormulario
from datetime import datetime
from django.shortcuts import get_object_or_404

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()
 
# Create your views here.
def inicio (request):
    posts =  BlogPost.objects.all()

    context = {'posts': posts}

    return render(request, "index.html", context)

def about (request):
    return render(request, "about.html")

def blogpost(request):
    msg = ''
    if request.method == "POST":
        
        form = BlogFormulario(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            datos_correctos = form.cleaned_data

            titulo = datos_correctos['titulo']
            subtitulo = datos_correctos['subtitulo']
            cuerpo = datos_correctos['cuerpo']
            autor = datos_correctos['autor']
            fecha = datetime.now()
            imagen = datos_correctos['imagen']
            
            post = BlogPost(titulo = titulo, 
                              subtitulo = subtitulo, 
                              cuerpo = cuerpo, 
                              autor = autor, 
                              fecha = fecha, 
                              imagen = imagen)
            post.save()
        
            msg = 'Se ha registrado el posteo satisfactoriamente!'
    else:
        form = BlogFormulario(user=request.user)
        msg = ''
        
    context = {'form': form, 'message': msg}

    return render(request, "blog_post.html", context)

class BlogCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogFormulario
    template_name = 'blog_post.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogView(DetailView):
    model = BlogPost
    template_name = "pages.html"
    context_object_name = "post"

class BlogDelete(DeleteView):
    model = BlogPost
    template_name = "post_delete.html"

    success_url = '/'

class BlogUpdate(UpdateView):
    model = BlogPost
    form_class = BlogFormulario
    template_name = "blog_post.html"

    def form_valid(self, form):
        form.save()
        print(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        errors = form.errors.as_data()
        for field, error in errors.items():
            print(f"{field}: {error}")
        return super().form_invalid(form)


    def get_success_url(self):
        return reverse_lazy('blogpost', kwargs={'pk': self.object.pk})

