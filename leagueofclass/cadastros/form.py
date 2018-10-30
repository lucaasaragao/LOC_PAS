import datetime

from django import forms
from django.forms import Form
from django.forms.widgets import ClearableFileInput
from .models import Aluno, Notas, Professor
from .models import Usuarios
from .models import Disciplinas
from .models import Perguntasx



class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Perguntasx
        exclude = ['matricula_professor']





class DisciplinaAlunoForm(forms.ModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        exclude = ['aluno', 'disciplina']
        #disciplina = forms.ModelChoiceField(queryset=Discplina.objects.all(), )
        #fields = '__all__'




class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
		#NÃO É PRECISO RECUPERAR TODOS OS FIELDS NESSE FORM O CADASTRO DE ALUNO, É MAIS SIMPLES QUE O DE PROFESSOR
		# É NECESSARIO O NOME DA INSTITUIÇÃO TAMBEM!
		#
		# form mais simples é isso #PAZ
		fields = [

		'nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao',

			];

class ProfessorForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo de formulario a partir do modelo que esta sendo criado no db;
	'''
	class Meta:
		model = Professor
		fields = ['nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao', 'matricula']

class UsuarioForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo do form de USers para autenticação!;
	'''
	class Meta:
		model = Usuarios
		fields = ['email','senha','matricula']
