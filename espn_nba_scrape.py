from bs4 import BeautifulSoup
import requests
import csv
from espn_ids import Espn_Scrape
from player import Player

# write year, month, and day as strings. If the string contains a single number like 3 then make sure to put a 0 in front of it.
year = input("Enter year such as 2018: ")
month = input("Enter month such as 03 for march: ")
day = input("Enter year such as 04 for the 4th day: ")
print(year)
print(month)
print(day)

# instantiating ESPN Scrape object that uses dynamic scraping to find the game id's
scrape = Espn_Scrape(year, month, day)
game_ids_list = scrape.find_game_ids()

#method that finds stats for pleayers
def find_player_stats(team, team_name):

	players_list = []
	#the starters and bench players
	starters = first_team.find_all('tbody')[0]
	bench = first_team.find_all('tbody')[1]

	rows = team.find_all('tr')

	for row in rows:
		name = row.find(class_='name')
		player_name = " "
		if not name.span == None:
			player_name = name.span.text
		elif name.text == 'TEAM':
			player_name = 'Team'

		position = row.find(class_='position')
		if not name.span == None:
			position = position.text

		minutes = row.find(class_='min')
		if not minutes == None:
			minutes = minutes.text

		field_goals = row.find(class_='fg')
		if not field_goals == None:
			field_goals = field_goals.text

		three_point = row.find(class_='3pt')
		if not three_point == None:
			three_point = three_point.text

		free_throw = row.find(class_='ft')
		if not free_throw == None:
			free_throw = free_throw.text

		off_rebound = row.find(class_='oreb')
		if not off_rebound == None:
			off_rebound = off_rebound.text

		def_rebound = row.find(class_='dreb')
		if not def_rebound == None:
			def_rebound = def_rebound.text

		rebounds = row.find(class_='reb')
		if not rebounds == None:
			rebounds = rebounds.text

		steals = row.find(class_='stl')
		if not field_goals == None:
			steals = steals.text

		blocks = row.find(class_='blk')
		if not field_goals == None:
			blocks = blocks.text

		turnovers = row.find(class_='to')
		if not turnovers == None:
			turnovers = turnovers.text

		points = row.find(class_='pts')
		if not points == None:
			points = points.text

		if player_name != " "  and player_name != "Team":
			player = Player(player_name, position, team_name, minutes, field_goals, three_point, free_throw, off_rebound, def_rebound, rebounds, steals, blocks, turnovers, points)
			players_list.append(player)
	return players_list

players_list = []

for game_id in game_ids_list:
	url = f"http://www.espn.com/nba/boxscore?gameId={game_id}"
	source = requests.get(url).text

	soup = BeautifulSoup(source, 'lxml')

	#goes to class named mod-data on espn 
	teams = soup.find_all(class_='mod-data')

	#theres 2 classes named mod-data so teams is a list of two items
	#this is the first class in teams
	first_team = teams[0]

	#this is the second class in teams
	second_team = teams[1]

	#finds table-caption classes which contains the team names
	team_names = soup.find_all(class_='table-caption')

	# extracts the team names
	first_team_name = team_names[0].text
	second_team_name = team_names[1].text

	temp_list = find_player_stats(first_team, first_team_name)

	temp_list2 = find_player_stats(second_team, second_team_name)

	index = 0
	while index < len(temp_list):
		players_list.append(temp_list[index])
		index +=1

	index = 0
	while index < len(temp_list2):
		players_list.append(temp_list2[index])
		index +=1

index = 0
with open(f"/Users/alexbetancourt/Documents/NBA_STATS/game_stats/player_stats_{year}-{month}-{day}.csv", 'w', newline='') as csvfile:
	fieldnames = ['first_name', 'last_name', 'position', 'player_team_name', 'minutes', 'three_pointers_made', 'three_pointers_attempted',
		     	  'free_throws_made', 'free_throws_attemped', 'offensive_rebounds', 'defensive_rebounds', 'total_rebounds', 'steals',
		     	  'blocks', 'turnovers', 'points']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	while index < len(players_list):
		if players_list[index].minutes != None or players_list[index].three_point != None:
			writer.writerow({'first_name': players_list[index].get_first_name(), 'last_name': players_list[index].get_last_name(), 'position': players_list[index].position,
	    				'player_team_name': players_list[index].player_team_name, 'minutes': players_list[index].minutes, 
	    				'three_pointers_made': players_list[index].get_three_pointers_made(), 'three_pointers_attempted': players_list[index].get_three_pointers_attempted(),
	    				'free_throws_made': players_list[index].get_free_throws_made(), 'free_throws_attemped': players_list[index].get_free_throws_attempted(),
	    				'offensive_rebounds': players_list[index].oreb, 'defensive_rebounds': players_list[index].dreb, 'total_rebounds': players_list[index].reb,
	    				'steals': players_list[index].stl, 'blocks': players_list[index].blk, 'turnovers': players_list[index].to, 'points': players_list[index].pts})
		else:
			writer.writerow({'first_name': players_list[index].get_first_name(), 'last_name': players_list[index].get_last_name(), 'position': players_list[index].position,
	    				'player_team_name': players_list[index].player_team_name, 'minutes': "Did not play"})
		index +=1



