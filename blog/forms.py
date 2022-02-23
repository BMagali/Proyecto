from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Post, Tag



# class PostFormulario(forms.Form):
#     titulo = forms.CharField()
#     subtitulo = forms.CharField()
#     texto = forms.CharField()
#     autor = forms.CharField()
#     # imagen = forms.ImageField()
#     tags = forms.CharField()


class PostFormulario(forms.ModelForm):
    class Meta :
        model = Post
        fields = ('titulo', 'subtitulo', 'texto', 'tags')
        widget = ({
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.Select(attrs={'class': 'form-control'}),
        })

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()
   
# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField()
#     email=forms.EmailField()
#     password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
#     firstname= forms.CharField()
#     lastname= forms.CharField()

#     class Meta:
#         Model = User
#         fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname']
#         help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label='Modificar e-mail')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    firstname= forms.CharField()
    lastname= forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'firstname', 'lastname']
        help_text = {k:"" for k in fields}

class Comentario(forms.Form):
    contenido = forms.TextInput()

   
