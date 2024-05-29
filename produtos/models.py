from django.db import models

# Create your models here.
class Celular(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    preco = models.IntegerField()
    imagem = models.URLField(max_length=300)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Celular"
        verbose_name_plural = "Celulares"