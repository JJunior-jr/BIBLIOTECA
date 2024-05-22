from django import forms
from .models import Livros

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        '''fields = ('nome', 'autor', 'editora', 'data_cadastro', 'emprestado', 'categoria')'''
        fields = "__all__" 
        
        
        '''neste caso posso escolher usar todos os campos'''