from django.contrib.auth.models import User
from django.db import models


class Imovel(models.Model):
    # infos referentes ao corretor
    corretor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    # infos referentes ao imóvel
    ref = models.CharField(max_length=7, default='')
    condominio = models.CharField(max_length=200, default='')
    cep = models.CharField(max_length=20, default='')
    cidade = models.CharField(max_length=20, default='')
    bairro = models.CharField(max_length=200, default='')
    endereco = models.CharField(max_length=200, default='')
    numero = models.CharField(max_length=15, default='')
    km = models.IntegerField(default='0')
    pt_referencia = models.CharField(max_length=200, default='')
    valor_venda = models.FloatField(default='')
    valor_aluguel = models.FloatField(default='')
    valor_condominio = models.FloatField(default='')
    valor_iptu = models.FloatField(default='')
    ano_construcao = models.DateField(default='')
    ano_reforma = models.DateField(default='')
    zfile = models.FileField(upload_to='uploads/', default='')
    
    # infos referentes ao proprietário
    nome = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=11, default='')
    email = models.CharField(max_length=200, default='')
    
    # infos adicionais
    observacoes = models.CharField(max_length=400, null=True, blank=True, default='')
    
    # infos referentes à interessa na permuta
    tipo_interesse = models.CharField(max_length=50, default='')
    regiao_interesse = models.CharField(max_length=50, default='')
    uf_interesse = models.CharField(max_length=2, default='')
    valor_minimo_interesse = models.IntegerField(default='')
    valor_maximo_interesse = models.IntegerField(default='')
    
    def __self__(self) -> str:
        return self.nome