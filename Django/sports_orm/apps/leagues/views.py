from django.shortcuts import render, redirect
from django.db.models import Count
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		#LEAGUES
		"atlanticsoccer": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"currentpenguins": Player.objects.filter(curr_team__team_name="Penguins"),
		"currentbaseballconference": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		
		"lopezfootballplayers": Player.objects.filter(last_name="Lopez").filter(curr_team__league__name="American Conference of Amateur Football"),
		"allfootballplayers": Player.objects.filter(curr_team__league__name__contains="Football"),

		"teamswithsophia": Team.objects.filter(curr_players__first_name__contains="Sophia"),
		"leagueswithsophia": League.objects.filter(teams__curr_players__first_name__contains="Sophia"),

		"flores": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),

		"samevansteams": Team.objects.filter(all_players__first_name="Samuel",all_players__last_name="Evans"),
		
		"tigercatsplayers": Player.objects.filter(all_teams__team_name="Tiger-Cats"),
		# "tigercatsplayers": Team.objects.filter(team_name="Tiger-Cats").all_players.all(),

		"wichitaformerplayers": Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings"),
		
		"jacobgrayformerteams": Player.objects.filter(first_name="Jacob", last_name="Gray")[0].all_teams.all().exclude(team_name="Colts"),

		"joshua": Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		
		"teamswith12": Team.objects.annotate(num_teams=Count("all_players")).filter(num_teams__gt=12),

		"countofteams": Player.objects.annotate(total_teams=Count('all_teams')).order_by("-total_teams")


		# ORM1
		# #LEAGUES
		# "leagues": League.objects.all(),
		# "baseball": League.objects.filter(sport="Baseball").all(),
		# "women": League.objects.filter(name__contains="Women").all(),
		# "hockey": League.objects.filter(name__contains="hockey").all(),
		# "exceptfootball": League.objects.all().exclude(sport="Football"),
		# "conferences": League.objects.filter(name__contains="conference"),
		# "atlantic": League.objects.filter(name__contains="atlantic"),
		# #TEAMS
		# "dallas": Team.objects.filter(location="Dallas"),
		# "raptors": Team.objects.filter(team_name__contains="Raptors"),
		# "city": Team.objects.filter(location__contains="city"),
		# "namedT": Team.objects.filter(team_name__startswith="T"),
		# "alphabetical": Team.objects.order_by("location"),
		# "rev": Team.objects.order_by("-team_name"),
		# #PLAYERS
		# "cooper": Player.objects.filter(last_name="Cooper"),
		# "joshua": Player.objects.filter(first_name="Joshua"),
		# "cooperexcept": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		# "alexanderwyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")