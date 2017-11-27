from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		#LEAGUES
		"leagues": League.objects.all(),
		"baseball": League.objects.filter(sport="Baseball").all(),
		"women": League.objects.filter(name__contains="Women").all(),
		"hockey": League.objects.filter(name__contains="hockey").all(),
		"exceptfootball": League.objects.all().exclude(sport="Football"),
		"conferences": League.objects.filter(name__contains="conference"),
		"atlantic": League.objects.filter(name__contains="atlantic"),
		#TEAMS
		"dallas": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name__contains="Raptors"),
		"city": Team.objects.filter(location__contains="city"),
		"namedT": Team.objects.filter(team_name__startswith="T"),
		"alphabetical": Team.objects.order_by("location"),
		"rev": Team.objects.order_by("-team_name"),
		#PLAYERS
		"cooper": Player.objects.filter(last_name="Cooper"),
		"joshua": Player.objects.filter(first_name="Joshua"),
		"cooperexcept": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexanderwyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")