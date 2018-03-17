from __future__ import print_function
import mlbgame
import tweepy, time, sys
import datetime
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY='zlSUYRhses1qZntTY0xr0beMc'
CONSUMER_SECRET='CwR4xjGdWU8urCbK6MQ1wUhYmgtpIWdSEvsahLhJfvs4eoYE5V'
ACCESS_TOKEN='975037851703431170-ZK7OJpNrkK9XdrzteWjBlU1tucvgF8f'
ACCESS_TOKEN_SECRET='ylPE7GrCKPfYGm579f8fx0MO5PRn5qPZ0toHK7pZtVx4W'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

football_scores = [0, 3, 6, 7, 10, 13, 14, 17, 20, 21, 24]

football_teams_and_home_parks = {
	"Cubs": ["Bears", "Wrigley Field"],
	"Angels": ["Chargers", "Angels Stadium"],
	"Astros": ["Texans", "Minute Maid Park"],
	"Athletics": ["Raiders", "Oakland Coliseum"],
	"Blue Jays": ["Argonauts", "Skydome"],
	"Brewers": ["Packers", "Miller Park"],
	"Cardinals": ["St. Louis Rams", "Busch Stadium"],
	"D-backs": ["Arizona Cardinals", "Chase Field"],
	"Dodgers": ["Rams", "Dodger Stadium"],
	"Giants": ["49ers", "AT&T Park"],
	"Indians": ["Browns", "Progressive Field"],
	"Mariners": ["Seahawks", "Safeco Field"],
	"Marlins": ["Dolphins", "Marlins Park"],
	"Mets": ["Jets", "Citi Field"],
	"Nationals": ["Washington football team", "Nationals Park"],
	"Phillies": ["Eagles", "Citizens Bank Park"],
	"Pirates": ["Steelers", "PNC Park"],
	"Orioles": ["Ravens", "Oriole Park at Camden Yards"],
	"Rangers": ["Cowboys", "The Ballpark in Arlington"],
	"Rays": ["Buccaneers", "Tropicana Field"],
	"Rockies": ["Broncos", "Coors Field"],
	"Royals": ["Chiefs", "Kauffman Stadium"],
	"Tigers": ["Lions", "Comerica Park"],
	"Yankees": ["New York Giants", "Yankee Stadium"],
	"Red Sox": ["Patriots", "Fenway Park"],
	"Reds": ["Bengals", "Great American Ballpark"],
	"Twins": ["Vikings", "Target Field"],
	"White Sox": ["Bears", "Guaranteed Rate Field"],
	"Braves": ["Falcons", "Suntrust Park"],
	"Padres": ["San Diego Chargers", "Petco Park"]
}

yesterday = datetime.datetime.now() - timedelta(days=1)
 
football_games = []

day = mlbgame.day(yesterday.year, yesterday.month, yesterday.day)
for game in day:
  if game.home_team_runs in football_scores and game.away_team_runs in football_scores and game.home_team_runs != game.away_team_runs:
    ballpark = football_teams_and_home_parks[game.home_team][1]
    big_score = max(game.away_team_runs, game.home_team_runs)
    little_score = min(game.away_team_runs, game.home_team_runs)
    if big_score == game.away_team_runs:
      winner = football_teams_and_home_parks[game.away_team][0]
      loser = football_teams_and_home_parks[game.home_team][0]
    else: 
      winner = football_teams_and_home_parks[game.away_team][0]
      loser = football_teams_and_home_parks[game.home_team][0]
    football_games.append("A football game broke out at {}! The {} beat the {}, {} to {}.".format(ballpark, winner, loser, big_score, little_score))

for line in football_games:
    api.update_status(line)
    time.sleep(30)