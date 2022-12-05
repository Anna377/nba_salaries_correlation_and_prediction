from lxml import html
import requests
import csv

years = [2022]

teamsDictionary = {
    'atlanta-hawks': 'ATL', 'boston-celtics': 'BOS', 'brooklyn-nets': 'BKN', 'charlotte-hornets': 'CHA',
    'chicago-bulls': 'CHI', 'cleveland-cavaliers': 'CLE', 'dallas-mavericks': 'DAL', 'denver-nuggets': 'DEN',
    'detroit-pistons': 'DET', 'golden-state-warriors': 'GSW', 'houston-rockets': 'HOU', 'indiana-pacers': 'IND',
    'los-angeles-clippers': 'LAC', 'los-angeles-lakers': 'LAL', 'memphis-grizzlies': 'MEM',
    'miami-heat': 'MIA', 'milwaukee-bucks': 'MIL', 'minnesota-timberwolves': 'MIN', 'new-jersey-nets': 'NJN',
    'new-orleans-hornets': 'NOP', 'new-york-knicks': 'NYK', 'oklahoma-city-thunder': 'OKC', 'orlando-magic': 'ORL',
    'philadelphia-76ers': 'PHI', 'phoenix-suns': 'PHX',
    'portland-trail-blazers': 'POR', 'sacramento-kings': 'SAC', 'san-antonio-spurs': 'SAS', 'toronto-raptors': 'TOR',
    'utah-jazz': 'UTH', 'washington-wizards': 'WAS'
}

positionsDictionary = {
    'Point Guard': 'PG', 'Shooting Guard': 'SG', 'Small Forward': 'SF',
    'Power Forward': 'PF', 'Center': 'C', 'Guard': 'G', 'Forward': 'F'
}

for year in years:

    url = 'http://www.spotrac.com/nba/free-agents/' + str(year) + '/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    players = tree.xpath('//tr/td//text()')
    lst = list(range(len(players)))
    totsalaries = []
    numTotsalaries = []
    salaries = []
    numberSalaries = []
    names = []
    positions = []
    teams = []
    ages = []
    status = []
    max_contract = []

    for i in lst:
        if players[i] in teamsDictionary.values() and players[i + 1] in teamsDictionary.values():
            if players[i - 3] in positionsDictionary.values():
                if len(players[i + 3]) > 2:
                    names.append(players[i - 4])
                    salaries.append(players[i + 4])## average
                    totsalaries.append(players[i + 3])
                    ages.append(players[i - 2])
                    status.append(players[i - 1])
                    positions.append(players[i - 3])
                    teams.append(players[i])
                    max_contract.append(players[i+5])

    with open(str(year) + ".csv", 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(
            ['last name', 'first name', 'age', 'position', 'team', 'faStatus', 'total-contract', 'average', 'max-contract'])

    for salary in salaries:
        s = salary.replace("$", "")
        s = s.replace(",", "")
        s = s.replace(" ", "")
        k = int(s)
        numberSalaries.append(k)

    for totsalary in totsalaries:
        s = totsalary.replace("$", "")
        s = s.replace(",", "")
        s = s.replace(" ", "")
        k = int(s)
        numTotsalaries.append(k)


    with open(str(year) + ".csv", 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(names)):
            fullName = names[i].split(" ")
            first = ""
            middle = ""
            last = ""

            first = fullName[0]
            if (len(fullName) == 3):
                middle = fullName[1]
                last = fullName[2]
            else:
                last = fullName[1]

            filewriter.writerow([middle + last, first, ages[i], positions[i], teams[i], status[i], numTotsalaries[i],
                                 numberSalaries[i], max_contract[i]])




