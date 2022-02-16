from dataclasses import fields
from venv import create
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Avatar, Post, Comentario, Tag
from blog.forms import AvatarFormulario, PostFormulario, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def inicio(request):
    
    return render(request, 'inicio.html')

def post(request):
    posts=Post.objects.all()
    return render(request, 'post.html', {"posts":posts})

def ShowPost(request, id):
    post=Post.objects.get(id=id)
    tags=Tag.objects.filter(post__id=id)
    return render(request, 'show.html', {"post":post, "tags":tags})

def comentario(request,id):
    comentario=Comentario.objects.get(id=id)
    return render(request, 'comentario.html', {"comentario":comentario})

# def postFormulario(request):
#     return render(request, "postFormulario.html")

@login_required
def postFormulario(request):
    if request.method == 'POST':
        miformulario = PostFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            inf = miformulario.cleaned_data
            post= Post(titulo=inf['titulo'], subtitulo=inf['subtitulo'], texto=inf['texto'])
            post.save()

            return render(request, "inicio.html")

    else:
        miformulario= PostFormulario()
    return render(request, "postFormulario.html", {"miformulario":miformulario})

def busquedaPost(request):
    return render(request, "busquedaPost.html")

def buscar(request):

    if request.GET["titulo"]:
        titulo = request.GET['titulo']
        posts= Post.objects.filter(titulo__icontains=titulo)

        return render(request, "resultadosbusqueda.html", {"posts":posts, "titulo":titulo})
    else:
        respuesta="No enviaste datos validos"
    return HttpResponse(respuesta)

def leerPosts(request):
    posts = Post.objects.all()
    contexto = {"posts":posts}
    
    return render(request, "leerPosts.html", contexto)

def eliminarPost(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()

    posts= Post.objects.all()
    contexto={"posts":posts}

    return render(request, "leerPosts.html", contexto)



class PostList(ListView):
    model = Post
    template_name = "posts_list.html"

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "posts_detalle.html"

class PostCreate(LoginRequiredMixin, CreateView):
    #form_model = PostFormulario
    model = Post
    success_url = '/post/list'
    fields = ['titulo', 'texto', 'imagen']
    template_name = "postFormulario.html"



class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post/list'
    template_name = "/"



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                
                return render(request, "inicio.html", {"mensaje":f"Bienvenid@ {usuario}"})

            else:
                return render(request, "inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:
                return render(request, "inicio.html", {"mensaje":"Error, datos incorrectos"} )
    else:
        form = AuthenticationForm()

        return render(request, "login.html", {'form':form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje":"¡Usuario creado con éxito!"})

    else:
        form = UserCreationForm()
        #form = UserRegisterForm()
    return render(request, "registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data


            usuario.email= info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.firstname = info['firstname']
            usuario.lastname = info['lastname']
            usuario.save()

            return render(request, "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def agregarImagen(request):
    if request.method=='POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)
            imagen = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            imagen.save()
            return render(request, "avatarView.html")

    else:
        miFormulario= AvatarFormulario()
        return render(request, "AgregarAvatar.html", {"miFormulario":miFormulario})

@login_required
def avatarView(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "avatarView.html", {"url":avatares[0].imagen.url})