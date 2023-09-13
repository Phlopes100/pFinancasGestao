from django.db import models

# Create your models here.
class Tipo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return  self.descricao


class Controle(models.Model):
    data = models.DateField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    observacao = models.CharField(max_length=100, null=True, blank=True)



