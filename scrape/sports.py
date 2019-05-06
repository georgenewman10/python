from sportsreference.nba.schedule import Schedule

por_schedule = Schedule('POR')
for game in por_schedule:
    print(game.date)
    print(game.time)
