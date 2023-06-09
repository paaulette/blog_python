from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from blog.models import BlogPost, Message
from .forms import BlogFormulario, MessageForm
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
 
# Create your views here.
@login_required(login_url='/accounts/login/')
def inicio (request):
    posts =  BlogPost.objects.all()

    context = {'posts': posts}

    return render(request, "index.html", context)

@login_required(login_url='/accounts/login/')
def about (request):
    return render(request, "about.html")

@login_required(login_url='/accounts/login/')
def blogpost (request):
    msg = ''
    if request.method == "POST":
        
        form = BlogFormulario(request.POST, request.FILES)

        if form.is_valid():
            datos_correctos = form.cleaned_data

            author = get_object_or_404(User, username= request.user.username)

            titulo = datos_correctos['titulo']
            subtitulo = datos_correctos['subtitulo']
            cuerpo = datos_correctos['cuerpo']
            autor = author
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
        form = BlogFormulario()
        msg = ''
        
    context = {'form': form, 'message': msg}

    return render(request, "blog_post.html", context)

class BlogView(DetailView):
    model = BlogPost
    template_name = "pages.html"
    context_object_name = "post"

class BlogDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = BlogPost
    template_name = "post_delete.html"

    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('/')

class BlogUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
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

@login_required
def messaging(request):
    users = User.objects.exclude(id=request.user.id)
    selected_user = None
    messages = None

    if request.method == "POST":
        recipient_id = request.POST.get("user_id")
        message_content = request.POST.get("message")
        
        recipient = User.objects.get(id=recipient_id)
        message = Message(sender=request.user, recipient=recipient, content=message_content)
        message.save()
        
        return redirect(f"/messages/?user_id={recipient_id}")

    user_id = request.GET.get("user_id")
    if user_id:
        selected_user = User.objects.get(id=user_id)
        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(recipient=selected_user)) |
            (Q(sender=selected_user) & Q(recipient=request.user))
        ).order_by("timestamp")

    context = {
        "users": users,
        "selected_user": selected_user,
        "messages": messages
    }

    return render(request, "messages.html", context)