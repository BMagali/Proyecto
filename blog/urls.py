from unicodedata import name
from django.urls import path
from blog import views as v
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', v.inicio, name="Home"),
    path('post/', v.post),
    path('ShowPost/<id>/', v.ShowPost, name="ShowPost"),
    path('comentario/<id>/', v.comentario),
    path('postFormulario/', v.postFormulario, name="PostFormulario"),
    path('busquedaPost/', v.busquedaPost, name="BusquedaPost"),
    path('buscar/', v.buscar),
   
    path('leerPosts/', v.leerPosts, name='LeerPosts'),
    path('eliminarPost/<post_id>/', v.eliminarPost, name="EliminarPost"),
   
    
    path('post/list', v.PostList.as_view(), name="List"),
    path('postdetalle/<pk>/', v.PostDetail.as_view(), name="Detail"),
    path('crear/', v.PostCreate.as_view(), name='Create'),
    path('eliminar/<pk>', v.PostDelete.as_view(), name='Delete'), #Uso el otro
    
    path('login/', v.login_request, name='Login'),
    path('register', v.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil/', v.editarPerfil, name='EditarPerfil'),

    path('agregarImagen/', v.agregarImagen, name='AgregarImagen'),
    path('avatarView/', v.avatarView, name='avatarView'),

]

