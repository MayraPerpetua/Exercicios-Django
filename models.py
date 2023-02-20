from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    matricula = models.IntegerField(default = 0)
    idade = models.IntegerField(default = 0)
    user = models.OneToOneField(User, blank = True, null = True, on_delete = models.CASCADE)
    nota1 = models.IntegerField(default = 0)
    nota2 = models.IntegerField(default = 0)
    nome = models.CharField(blank = True, max_length= 80)

    def __str__(self):
        return '({}) - {} - {}'.format(self.id, self.matricula, self.CalcMedia(self.nota1, self.nota2))


    def CalcMedia(self, nota1, nota2):
        resultado = ((nota1 * 0.6) + (nota2 * 0.4))
        if (resultado >= 60):
            return "Aprovado"
        else:
            return "Reprovado"