from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/auth/login')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')