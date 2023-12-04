from .models import Permuta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required(login_url='/auth/login')
def nova_permuta(request):
    if request.method == 'GET':
        return render(request, 'nova_permuta.html')
    
    elif request.method == 'POST':
        ref = request.POST.get('ref')
        condominio = request.POST.get('condominio')
        endereco = request.POST.get('endereco')
        uf = request.POST.get('uf')
        tipo = request.POST.get('tipo')
        regiao = request.POST.get('regiao')
        valor_venda = request.POST.get('valor_venda')
        valor_aluguel = request.POST.get('valor_aluguel')
        valor_condominio = request.POST.get('valor_condominio')
        valor_iptu = request.POST.get('valor_iptu')
        ano_construcao = request.POST.get('ano_construcao')
        ano_reforma = request.POST.get('ano_reforma')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacoes = request.POST.get('observacoes')
        zfile = request.FILES.get('zfile')
        km_interesse = request.POST.get('km_interesse')
        valor_minimo_interesse = request.POST.get('valor_minimo_interesse')
        valor_maximo_interesse = request.POST.get('valor_maximo_interesse')
        
        permuta = Permuta(
            corretor = request.user,
            condominio = condominio,
            endereco = endereco,
            uf = uf,
            tipo = tipo,
            regiao = regiao,
            valor_venda = valor_venda,
            valor_aluguel = valor_aluguel,
            valor_condominio = valor_condominio,
            valor_iptu = valor_iptu,
            ano_construcao = ano_construcao,
            ano_reforma = ano_reforma,
            nome = nome,
            telefone = telefone,
            email = email,
            observacoes = observacoes,
            zfile = zfile,
            km_interesse = km_interesse,
            valor_minimo_interesse = valor_minimo_interesse,
            valor_maximo_interesse = valor_maximo_interesse,
        )
        permuta.save()
        messages.add_message(request, constants.SUCCESS, 'Permuta cadastrada com sucesso!')
        return render(request, 'nova_permuta.html')


@login_required(login_url='/auth/login')
def permutas(request):
    if request.method == "GET":
        regiao_filtrada = request.GET.get('regiao_filtrada')
        tipo_filtrado = request.GET.get('tipo_filtrado')
        km_interesse = request.GET.get('km_interesse')
        valor_interesse = request.GET.get('valor_interesse')
        permutas = Permuta.objects.all()
        
        if regiao_filtrada:
            permutas = permutas.filter(regiao__contains=regiao_filtrada)
        
        if tipo_filtrado:
            permutas = permutas.filter(tipo__contains=tipo_filtrado)
            
        if km_interesse:
            permutas = permutas.filter(km_interesse=km_interesse)
            
        if valor_interesse:
            permutas = permutas.filter(valor_interesse=valor_interesse)
        
        return render(request, 'permutas.html',
                      {'permutas':permutas}
                      )


@login_required(login_url='/auth/login')
def minhas_permutas(request):
    if request.method == "GET":
        regiao_filtrada = request.GET.get('regiao_filtrada')
        tipo_filtrado = request.GET.get('tipo_filtrado')
        km_interesse = request.GET.get('km_interesse')
        valor_interesse = request.GET.get('valor_interesse')
        
        permutas = Permuta.objects.filter(corretor=request.user)
        
        if regiao_filtrada:
            permutas = permutas.filter(regiao__contains=regiao_filtrada)
        
        if tipo_filtrado:
            permutas = permutas.filter(tipo__contains=tipo_filtrado)
            
        if km_interesse:
            permutas = permutas.filter(km_interesse=km_interesse)
            
        if valor_interesse:
            permutas = permutas.filter(valor_interesse=valor_interesse)
        
        return render(request, 'minhas_permutas.html',
                      {'permutas':permutas}
                      )