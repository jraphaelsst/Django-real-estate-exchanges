from .models import Imovel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required(login_url='/auth/login')
def novo_imovel(request):
    if request.method == 'GET':
        return render(request, 'novo_imovel.html')
    
    elif request.method == 'POST':
        ref = request.POST.get('ref')
        km = request.POST.get('km')
        condominio = request.POST.get('condominio')
        endereco = request.POST.get('endereco')
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
        tipo_interesse = request.POST.get('tipo_interesse')
        regiao_interesse = request.POST.get('regiao_interesse')
        uf_interesse = request.POST.get('uf_interesse')
        valor_minimo_interesse = request.POST.get('valor_minimo_interesse')
        valor_maximo_interesse = request.POST.get('valor_maximo_interesse')
        
        imovel = Imovel(
            ref = ref,
            km = km,
            corretor = request.user,
            condominio = condominio,
            endereco = endereco,
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
            tipo_interesse = tipo_interesse,
            regiao_interesse = regiao_interesse,
            uf_interesse = uf_interesse,
            valor_minimo_interesse = valor_minimo_interesse,
            valor_maximo_interesse = valor_maximo_interesse,
        )
        imovel.save()
        messages.add_message(request, constants.SUCCESS, 'Imóvel cadastrado com sucesso!')
        return render(request, 'novo_imovel.html')


@login_required(login_url='/auth/login')
def imoveis(request):
    if request.method == "GET":
        
        condominio_filtrado = request.GET.get('condominio_filtrado')
        km_filtrado = request.GET.get('km_filtrado')
        
        uf_interesse = request.GET.get('uf_interesse')
        regiao_interesse = request.GET.get('regiao_interesse')
        tipo_interesse = request.GET.get('tipo_interesse')
        valor_minimo_interesse = request.GET.get('valor_minimo_interesse')
        valor_maximo_interesse = request.GET.get('valor_maximo_interesse')
        
        imoveis = Imovel.objects.all()
        
        if condominio_filtrado:
            imoveis = imoveis.filter(condominio__contains=condominio_filtrado)
        
        if km_filtrado:
            imoveis = imoveis.filter(km=km_filtrado)
        
        if uf_interesse:
            imoveis = imoveis.filter(uf_interesse=uf_interesse)
        
        if regiao_interesse:
            imoveis = imoveis.filter(regiao_interesse__contains=regiao_interesse)
        
        if tipo_interesse:
            imoveis = imoveis.filter(tipo_interesse__contains=tipo_interesse)
        
        if valor_minimo_interesse:
            imoveis = imoveis.filter(valor_minimo_interesse__gte=valor_minimo_interesse)
        
        if valor_maximo_interesse:
            imoveis = imoveis.filter(valor_maximo_interesse__lte=valor_maximo_interesse)
        
        
        return render(request, 'imoveis.html',
                      {'imoveis':imoveis}
                      )


@login_required(login_url='/auth/login')
def meus_imoveis(request):
    if request.method == 'GET':
        
        condominio_filtrado = request.GET.get('condominio_filtrado')
        km_filtrado = request.GET.get('km_filtrado')
        
        uf_interesse = request.GET.get('uf_interesse')
        regiao_interesse = request.GET.get('regiao_interesse')
        tipo_interesse = request.GET.get('tipo_interesse')
        valor_minimo_interesse = request.GET.get('valor_minimo_interesse')
        valor_maximo_interesse = request.GET.get('valor_maximo_interesse')
        
        imoveis = Imovel.objects.filter(corretor=request.user)
        
        if condominio_filtrado:
            imoveis = imoveis.filter(condominio__contains=condominio_filtrado)
        
        if km_filtrado:
            imoveis = imoveis.filter(km=km_filtrado)
        
        if uf_interesse:
            imoveis = imoveis.filter(uf_interesse=uf_interesse)
        
        if regiao_interesse:
            imoveis = imoveis.filter(regiao_interesse__contains=regiao_interesse)
        
        if tipo_interesse:
            imoveis = imoveis.filter(tipo_interesse__contains=tipo_interesse)
        
        if valor_minimo_interesse:
            imoveis = imoveis.filter(valor_minimo_interesse__gte=valor_minimo_interesse)
        
        if valor_maximo_interesse:
            imoveis = imoveis.filter(valor_maximo_interesse__lte=valor_maximo_interesse)
        
        return render(request, 'meus_imoveis.html',
                      {'imoveis':imoveis}
                      )
