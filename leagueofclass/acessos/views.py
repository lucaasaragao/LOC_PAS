import sys
sys.path.append('../')

from cadastros.models import Aluno, Frequencia, Disciplinas, Notas, Professor
from cadastros.form import NotasForm

from django.shortcuts import render, redirect
from django.contrib.auth import logout



def failUserXFF(request):

    return render(request,'leagueofclass/failAutenticate.html')


def logoutUser(request):
    if request.user != None:
        logout(request)
    return redirect('/index')

def chosePerfil(request):
    return render(request,'leagueofclass/telaescolha.html')


def acessoAluno(request):
    data = {}
    #ideia... fazer um filter que compare request.user com o usuário o login
    data['exibeInicio'] = True
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = False
    data['msg'] = 'Suas informações:'
    data['alunos'] = Aluno.objects.filter(nome=request.user)
    data['usuario'] = request.user
    return render(request,'leagueofclass/painel_aluno.html', data)

def acessoProfessor(request):
    data = {}
    #ideia... fazer um filter que compare request.user com o usuário o login
    data['exibeInicio'] = True
    data['msg'] = 'Suas informações'
    data['professor'] = Professor.objects.filter(nome=request.user)
    data['usuario'] = request.user
    return render(request,'leagueofclass/painel_professor.html', data)

def notasAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = True
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = False
    data['msg'] = 'Escolha uma disciplina para visualizar suas notas:'
    data ['qsDisciplinas'] = Disciplinas.objects.filter(aluno__nome__exact=request.user)

    if request.method == 'POST':
        disciplinaEsc = request.POST.get('notasDisc', 'null')
        data['exibeNotasDisciplina'] = True
        data['msg2'] = disciplinaEsc
        data['qsNotas'] = Notas.objects.filter(aluno__nome__exact=request.user).filter(disciplina__nomeDisciplina__exact=disciplinaEsc)
    return render(request,'leagueofclass/painel_aluno.html', data)

def opcCadNota(request):
    data = {}
    data['exibeOpcCadNota'] = True
    data['msg'] = 'Escolha uma disciplina para lançar as notas:'
    data['qsDisciplinas'] = Disciplinas.objects.filter(professor__nome__exact=request.user)
    return render(request,'leagueofclass/painel_professor.html', data)

def cadNotas(request):
    data = {}
    data['exibeNotas'] = True
    if request.method == 'POST':
        if 'form2' in request.POST:
            data['disciplina'] = request.POST.get('disciplina', '')
            data['aluno'] = request.POST.get('aluno', '')
            data['nota1'] = request.POST.get('nota1', '')
            data['nota2'] = request.POST.get('nota2', '')
            data['nota3'] = request.POST.get('nota3', '')
            data['media'] = request.POST.get('media', '')
            aluno = Aluno.objects.get(nome=data['aluno'])
            disciplina = Disciplinas.objects.get(nomeDisciplina=data['disciplina'])
            Notas.objects.create(aluno=aluno, disciplina=disciplina, nota1=data['nota1'], nota2=data['nota2'], nota3=data['nota3'], media=data['media'] )

            '''
            notas = NotasForm(request.POST)
            if notas.is_valid():
                notas.save()
                return redirect ('/home')
            else:
                notas = NotasForm()
                '''
    if request.method == 'POST':
        if 'form1' in request.POST:
            request.session['nomeDisc'] = request.POST.get('discEscolhida')
            data['exibeNotas'] = True
            data['nomeDisc'] = request.session.get('nomeDisc')
            try:
                data['disciplina'] = Disciplinas.objects.get(nomeDisciplina=request.session.get('nomeDisc'))
                disciplina = Disciplinas.objects.get(nomeDisciplina=request.session.get('nomeDisc'))
                data['alunos'] = disciplina.aluno.all()
            except Disciplinas.DoesNotExist:
                return redirect("/dashboardProfessor")

    return render(request,'leagueofclass/painel_professor.html', data)


def disciplinasAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = True
    data['exibeFrequencia'] = False
    data['disciplinas'] = Disciplinas.objects.filter(aluno__nome__exact=request.user)
    data['msg'] = 'Disciplinas Matriculadas:'
    return render(request,'leagueofclass/painel_aluno.html', data)

def cadDiscAluno(request):
    data = {}
    data['exibecadDiscAluno'] = True
    data['msg'] = 'Escolha em qual disciplina você quer se matricular:'
    data['qsDisciplinas'] = Disciplinas.objects.all()
    if request.method == "POST":
        if "form3" in request.POST:
            aluno = Aluno.objects.get(nome=request.user)
            disciplina = Disciplinas.objects.get(nomeDisciplina=request.POST.get('nomeDisciplina'))
            disciplina.aluno.add(aluno)

    return render(request,'leagueofclass/painel_aluno.html', data)

def frequenciaAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = True
    data ['qsDisciplinas'] = Disciplinas.objects.filter(aluno__nome__exact=request.user)
    data ['msg'] = 'Escolha uma discipina para ver a frequência:'

    if request.method == 'POST':
        disciplinaEsc = request.POST.get('freqDisc', 'null')
        data['exibeFreqDisciplina'] = True
        data['msg2'] = disciplinaEsc
        data['qsFreqDisciplinas'] = Frequencia.objects.filter(aluno__nome__exact=request.user).filter(disciplina__nomeDisciplina__exact=disciplinaEsc)
    return render(request,'leagueofclass/painel_aluno.html', data)

def cadDisciplina(request):
    data = {}
    data ['exibeCadDisc'] = True

    if request.method == 'POST':
        nomeDisciplina = request.POST.get('nomeDisciplina', 'null')
        professor = Professor.objects.get(nome=request.user)
        Disciplinas.objects.create(nomeDisciplina=nomeDisciplina, professor=professor)

    return render(request, 'leagueofclass/painel_professor.html', data)

def lancarFreq(request):
    data = {}
    data ['exibeOpcFrequencia'] = True
    data['qsDisciplinas'] = Disciplinas.objects.filter(professor__nome__exact=request.user)
    '''
    #ideia... fazer um filter que compare request.user com o usuário o login
    data['exibeLancaFreq'] = True
    data['msg'] = 'Frequência'
    data['qsDisciplinas'] = Disciplinas.objects.filter(professor__nome__exact=request.user)
    qsDisciplinas = Disciplinas.objects.get(professor__nome__exact=request.user) #queryset necessário para pegar os alunos cadastrados na disciplina do professor
    data['qsAluno'] = qsDisciplinas.aluno.all() #todos os alunos que estão cadastrados na disciplina do professor
    '''
    if request.method == 'POST':
        if 'form3' in request.POST:
            data['exibeLancaFreq'] = True
            data ['exibeOpcFrequencia'] = False
            data['msg'] = 'Frequência:'
            data['nomeDisciplina'] = request.POST.get('disciplinaFreq', 'null')
            request.session['disciFreq'] = request.POST.get('disciplinaFreq', 'null')
            disciplina = Disciplinas.objects.get(professor__nome__exact=request.user, nomeDisciplina=data['nomeDisciplina']) #queryset necessário para pegar os alunos cadastrados na disciplina do professor
            data['qsAluno'] = disciplina.aluno.all() #todos os alunos que estão cadastrados na disciplina do professor

    if request.method == 'POST':
        if 'form4' in request.POST:
            nomeAluno = request.POST.get('aluno', 'null')
            nomeDisciplina = request.session.get('disciFreq')
            dataF = request.POST.get('data', 'null') #dataF pra não misturar com o dicionário data = {}
            presenca = request.POST.get('presenca', 'null')

            aluno = Aluno.objects.get(nome=nomeAluno)
            disciplina = Disciplinas.objects.get(nomeDisciplina=nomeDisciplina)
            Frequencia.objects.create(frequencia=presenca, aluno=aluno, disciplina=disciplina, data=dataF)

    return render(request,'leagueofclass/painel_professor.html', data)


def atividadesAluno(request):
    return render(request,'leagueofclass/painel_aluno.html')

def clickMe(request):
    return render(request,'click.html')
