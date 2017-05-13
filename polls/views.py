from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Zawodnik
from .models import Zespol
from .models import TypZdarzenia
from .models import Mecz
from .models import Zdarzenie



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_view(request):
    return render(request, 'polls/home.html')

def base_view(request):
    return render(request, 'polls/base.html')

def show_player(request):
    zawodniki=Zawodnik.objects.all()
    return render(request,'polls/players.html',{'players':zawodniki})

def show_teams(request):
    teams=Zespol.objects.all()
    return render(request,'polls/teams.html',{'teams':teams})

def show_match(request):
    match=Mecz.objects.all()
    return render(request,'polls/match.html',{'match':match})



