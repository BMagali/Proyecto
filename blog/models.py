
from django.db import models
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=40)



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(null=True, blank=False, max_length=100)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True) 
    tags = models.ManyToManyField(Tag)
   
    def __str__(self):
        return f'Titulo:{self.titulo} - Subtitulo:{self.titulo} - Texto:{self.texto} - Tag:{self.tags}'
 

class Comentario(models.Model):
    contenido = models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null='True', blank='True')

    def __str__(self):
        return f"Imagen de: {self.user.username}"

# class Imagen(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='imagenes', null='True', blank='True')