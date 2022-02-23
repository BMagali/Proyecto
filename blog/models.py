
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Tag(models.Model):
    name = models.CharField(max_length=40)



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(null=True, blank=False, max_length=100)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
   
    def __str__(self):
        return f'Titulo:{self.titulo} - Subtitulo:{self.titulo} - Texto:{self.texto} - Tag:{self.tags}'

    def get_absolute_url(self):
        return reverse('Detail', args=(str(self.id)))
 

class Comentario(models.Model):
    contenido = models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null='True', blank='True')

    def __str__(self):
        return f"Imagen de: {self.user.username}"

