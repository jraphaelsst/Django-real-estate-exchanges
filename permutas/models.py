from django.contrib.auth.models import User
from django.db import models


class Permuta(models.Model):
    # infos referentes ao corretor
    corretor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    # infos referentes à permuta
    ref = models.CharField(max_length=7, default='')
    tipo = models.CharField(max_length=30, default='')
    uf = models.CharField(max_length=2, default='')
    regiao = models.CharField(max_length=80, default='')
    endereco = models.CharField(max_length=200, default='')
    condominio = models.CharField(max_length=80, default='')
    valor_venda = models.FloatField(default=0)
    valor_aluguel = models.FloatField(default=0)
    valor_condominio = models.FloatField(default=0)
    valor_iptu = models.FloatField(default=0)
    ano_construcao = models.DateField()
    ano_reforma = models.DateField()
    zfile = models.FileField(upload_to='uploads/', default=None)
    
    # infos referentes ao proprietário
    nome = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=11, default='')
    email = models.CharField(max_length=200, default='')
    
    # infos adicionais
    observacoes = models.CharField(max_length=400, null=True, blank=True, default='')
    
    # infos referentes ao imóvel de interesse
    km_interesse = models.IntegerField(default=0)
    valor_minimo_interesse = models.IntegerField(default=0)
    valor_maximo_interesse = models.IntegerField(default=0)
    
    def __self__(self) -> str:
        return self.nome