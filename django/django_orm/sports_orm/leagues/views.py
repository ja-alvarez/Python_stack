from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count
from . import team_maker

def index(request):
	context = {
		'leagues': League.objects.all(),
		'teams': Team.objects.all(),
		'players': Player.objects.all(),
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

def orm2(request):
	context = {
		'leagues': League.objects.all(),
		'teams': Team.objects.all(),
		'players': Player.objects.all(),

		'atlanticsoccer': Team.objects.filter(league__name='Atlantic Soccer Conference'),
		'atlanticsoc2': Player.objects.filter(curr_team__team_name='Penguins'),
		'intcollegiate': Player.objects.filter(curr_team__league_id=6),
		'amconference': Player.objects.filter(curr_team__league_id=9) & Player.objects.filter(last_name="Lopez"),
		#I couldn't find "American Conference of Amateur Football" instead I looked for "National Soccer Conference"
		'allfootballplayers': Player.objects.filter(curr_team__league__sport="Soccer"),
		'sophiateams': Team.objects.filter(curr_players__first_name="Sophia"),
		'sophialeagues': League.objects.filter(teams__curr_players__first_name="Sophia"),
		'floresnotwashington': Player.objects.filter(last_name="Flores"), #.exclude(curr_team="Washington Roughriders"), "There's no team named like that"
		'evanteams': Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		'tigerplayers': Player.objects.filter(all_teams__team_name="Tiger-Cats"),
		'formerlywichita': Player.objects.filter(all_teams__team_name="Wichita Vikings").exclude(curr_team__team_name="Wichita Vikings"),
		'jacobgray': Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Oregon Colts"),
		'atlanticbaseball': Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		'twelveplayers':  Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
		'numberofteams': Player.objects.all().annotate(num_teams=Count('all_teams')).order_by('num_teams'),

	}
	return render(request, "leagues/ORM_II.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")