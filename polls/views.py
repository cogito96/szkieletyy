from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

#from django import template

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
    players = Zawodnik.objects.all()
    teams = Zespol.objects.all()
    return render(request,'polls/players.html',{'players':players, 'teams':teams})

def show_teams(request):
    teams = Zespol.objects.all()
    return render(request,'polls/teams.html',{'teams':teams})

def show_match(request):
    match = Mecz.objects.all()
    return render(request,'polls/match.html',{'match':match})

def show_table(request):
    teams = Zespol.objects.all()
    list = [(team.licz_punkty(),team.nazwa_klubu) for team in teams]
    list.sort()
    list.reverse()
    return render (request,'polls/table.html',{'list':list})

def show_action(request):
    mecze = Mecz.objects.all()
    list = [(mecz.licz(),mecz,mecz.zespol_gospodarz,mecz.zespol_gosc) for mecz in mecze]
    return render (request,'polls/action.html',{'action':list})


def show_statistic(request):
    mecze = Mecz.objects.all()
    list = [(mecz.statystyki(),mecz,mecz.zespol_gospodarz,mecz.zespol_gosc) for mecz in mecze]
    return render (request,'polls/statistic.html',{'statistic':list})

def show_all_statistic(request):
    zawodnicy = Zawodnik.objects.all()
    list = [(zawodnik.liczz(),zawodnik) for zawodnik in zawodnicy]
    list.sort()
    list.reverse()
    return render (request,'polls/results.html',{'results':list})
