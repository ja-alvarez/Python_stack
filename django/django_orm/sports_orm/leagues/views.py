from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'baseball_leagues': League.objects.filter(sport='Baseball'),
		'women_leagues': League.objects.filter(name__contains='Women'),
		'typeofhockey': League.objects.filter(sport__contains='Hockey'),
		'othersports': League.objects.exclude(sport='Soccer'),
		'conferences': League.objects.filter(name__contains='Conference'),
		'atlanticregion': League.objects.filter(name__contains="atlantic"),
		'teamsindallas': Team.objects.filter(location='Dallas'),
		'raptors': Team.objects.filter(team_name__contains='Raptors'),
		'city': Team.objects.filter(location__contains='City'),
		'teams2': Team.objects.filter(team_name__startswith="T"),
		'orderedteam': Team.objects.all().order_by('location'),
		'reverse': Team.objects.all().order_by('-team_name'),
		'cooper': Player.objects.filter(last_name='Cooper'),
		'firstname': Player.objects.filter(first_name='Joshua'),
		'notjoshua': Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		'alexanderwyatt': Player.objects.filter(Q(first_name='Alexander') | Q(first_name='Wyatt')),








	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")