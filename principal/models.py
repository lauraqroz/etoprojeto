from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

#Classes

class Cliente(AbstractUser):
    email = models.EmailField(('email address'), unique=True)   
    endereco = models.CharField ('endereco', max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Colaborador(models.Model):
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome_colaborador = models.CharField(max_length=150)
    email_colaborador = models.EmailField()
    telefone_colaborador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_colaborador 

    class Meta:
        verbose_name_plural = 'Colaboradores'

class CarrinhoCompras(models.Model):
    produto = models.ForeignKey
    total_pedido = models.DecimalField


class Categoria (models.Model):
    nome = models.CharField (max_length=80)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField (max_length=50)
    preco = models.DecimalField ('Preço do produto', max_digits=4, decimal_places=2)
    quantidade = models.FloatField 
    categoria = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to='prdadmin/', blank=True, null=True, max_length=200)

    def __str__(self) -> str:
        return self.nome




    