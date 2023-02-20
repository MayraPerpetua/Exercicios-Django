from django.shortcuts import render, redirect
from django.views import View
from .models import Aluno
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'testepratico/index.html')


    def post(self, request, *args, **kwargs):
        #nome = request.POST.get('username')
        matricula = request.POST.get('matricula')
        idade = request.POST.get('idade')
        disciplina = request.POST.get('disciplina')
        nota1 = request.POST.get('nota1')
        nota2 = request.POST.get('nota2')

        #usuario = User.objects.create_user(username=nome, password=f'{matricula}' )
        #usuario.save()
        aluno = Aluno(idade=idade, matricula=matricula, nome=disciplina, nota1=nota1, nota2=nota2)
        aluno.save()

        return redirect('/testepratico/media')


class Media(View):
    def get(self, request, *args, **kwargs):
        contexto = {'alunos': Aluno.objects.all()}
        return render(request, 'testepratico/media.html', contexto)