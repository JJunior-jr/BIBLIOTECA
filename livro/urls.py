# o "."(ponto) referencia a propria pasta pois há diversos arquivos "urls" em diversas pastas
# podendo ser usadndo tambem como "from livro import views"

from django.urls import path
from .import views



urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_livro/<int:id>', views.ver_livros, name = 'ver_livros' ),
    path('cadastrar_livro', views.cadastrar_livro, name='cadastrar_livro')

]