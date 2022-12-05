from lxml import html
import requests
import csv

years = [2022]

for year in years:

    url = 'http://www.spotrac.com/nba/free-agents/' + str(year) + '/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    players = tree.xpath('//tr/td[@class= " player"]//text()')
    lst = list(range(len(players)))

    names = list(players)

    with open(str(year) + ".csv", 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['last name', 'first name'])

    with open(str(year) + ".csv", 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(names)):
            if names[i] != "    ":
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
                filewriter.writerow([middle + last, first])


