from django.shortcuts import render
from .models import Aluno,Professor,Perguntasx
from .form import AlunoForm,DisciplinaAlunoForm,AtividadeForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.shortcuts import redirect
from .form import UsuarioForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

'''
 __VAR__
'''
user_aut=''
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def cadastroProfessor(request):
	#url cadastro/ retorna o template de cadastros Professor!
	#Ñ implementada ainda


	if request.method=="POST":
		form = ProfessorForm(request.POST)

		if form.is_valid():

				try:

					verificaExistenciaPass = User.objects.get(password=form.cleaned_data['password'])
					verificaExistencia = User.objects.get(email=form.cleaned_data['email'])

					if verificaExistenciaPass or verificaExistencia:
						return render(request,'/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


				except User.DoesNotExist:
					nome_professor = form.cleaned_data['nome']
					email_professor = form.cleaned_data['email']
					password_professor = form.cleaned_data['password']
					new_professor = User.objects.create_user(username=nome_professor, email=email_professor,
															 password=password_professor)

					new_professor.save()
					form.save()
					return redirect("/home")




		else:
			messages.warning(request, 'Preencha todos os campos corretamente!')

	else:
		form = ProfessorForm()
	return render(request,'leagueofclass/cadastroprofessor.html' , {'form':form})

dados_aluno_necessario={}
def cadastroAluno(request):
	if request.method=="POST":
		form = AlunoForm(request.POST)


		if form.is_valid():
			try:


				verificaExistencia = User.objects.get(email=form.cleaned_data['email'])
				verificaExistenciaPass = User.objects.get(email=form.cleaned_data['email']).password
				if verificaExistenciaPass or verificaExistencia:
					return render(request, '/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


			except User.DoesNotExist:
				nome_aluno = form.cleaned_data['nome']
				email_aluno = form.cleaned_data['email']
				password_aluno = form.cleaned_data['password']
				new_aluno = User.objects.create_user(username=nome_aluno, email=email_aluno,
														 password=password_aluno)

				new_aluno.save()
				form.save()
				return redirect("/home")
		else:
			messages.warning(request, 'Preencha todos os campos corretamente!')
	else:
		form = AlunoForm()


	return render(request,'leagueofclass/cadastroaluno.html', {'form':form})


def createAuthentic(request):
	# Responsavel por criar a autenticaçao do usuario!



	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			object_user = User.objects.get(email=form.cleaned_data['email'])
			user_aut = authenticate(username=object_user.username, password=form.cleaned_data['senha'])
			try:
				professor_matricula = Professor.objects.get(email=form.cleaned_data['email']).matricula


				if user_aut is not None and professor_matricula!=None:
					login(request, user_aut)
					return redirect('/dashboardProfessor')

				else:
					messages.warning(request, 'Email ou Senha errados!')
					return redirect('/failUser')
			except Professor.DoesNotExist:
				if user_aut is not None:
					login(request,user_aut)
					return redirect('/dashboardAluno')
				else:
					messages.warning(request, 'Email ou Senha errados!')
					return redirect('/failUser')

	else:
		form = UsuarioForm()

	return render(request, 'index.html', {'form': form})

def cadastroAtividade(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			form = AtividadeForm(request.POST,request.FILES)
			if form.is_valid():

				titulo = form.cleaned_data['titulo']
				observacoes = form.cleaned_data['observacoes']
				instrucoes = form.cleaned_data['instrucoes']
				data_entrega = form.cleaned_data['data_entrega']

				professor=request.user
				if professor!= None:
					param=Professor.objects.get(email=request.user.email)
					if  param.matricula != None:

						perguntas = Perguntasx(matricula_professor=param.matricula,titulo=titulo,observacoes=observacoes,
											   instrucoes=instrucoes,data_entrega=data_entrega,atividade=request.FILES['atividade'])
						Perguntasx.save(perguntas)
						return redirect("/dashboardProfessor")
					else:
						return redirect("/error")
		else:
			form = AtividadeForm()

	return render(request, 'leagueofclass/cadastroAtividade.html', {'form': form})


def cadastroDisciplinaAluno(request):
    # form
	return render(request,"leagueofclass/cadastrarDisciplina.html")

def lancarAtividades(request):
	caminhoBase="/Documentos/"
	data_p = {}
	list_atividades=[]
	list_paths_encontrados=[]
	list_path_completa=[]
	if request.method=="GET":
		if request.user.is_authenticated:
			professor=request.user
			if professor!=None:
				param = Professor.objects.get(email=request.user.email)
				if param.matricula != None:
					atividades = Perguntasx.objects.filter(matricula_professor=param.matricula)
					for atividade in atividades:
						list_atividades.append(atividade)

					for paths in list_atividades:
						if paths != False:
							list_paths_encontrados.append(str(paths.atividade))

					for paths_find in list_paths_encontrados:
						complete = caminhoBase+paths_find
						list_path_completa.append(complete)

					data_p['exibirPaths'] = True
					data_p['user'] = request.user
					data_p['paths'] = list_path_completa

					return render(request,"leagueofclass/lancarAtividades.html", data_p)
