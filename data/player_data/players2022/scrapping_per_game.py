from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
from pathlib import Path

teamsDictionary = {
    'atlanta-hawks': 'ATL', 'boston-celtics': 'BOS', 'brooklyn-nets': 'BRK', 'charlotte-hornets': 'CHO',
    'chicago-bulls': 'CHI', 'cleveland-cavaliers': 'CLE', 'dallas-mavericks': 'DAL', 'denver-nuggets': 'DEN',
    'detroit-pistons': 'DET', 'golden-state-warriors': 'GSW', 'houston-rockets': 'HOU', 'indiana-pacers': 'IND',
    'los-angeles-clippers': 'LAC', 'los-angeles-lakers': 'LAL', 'memphis-grizzlies': 'MEM', 'miami-heat': 'MIA',
    'milwaukee-bucks': 'MIL', 'minnesota-timberwolves': 'MIN', 'new-orleans-hornets': 'NOP', 'new-york-knicks': 'NYK',
    'oklahoma-city-thunder': 'OKC', 'orlando-magic': 'ORL', 'philadelphia-76ers': 'PHI', 'phoenix-suns': 'PHO',
    'portland-trail-blazers': 'POR', 'sacramento-kings': 'SAC', 'san-antonio-spurs': 'SAS', 'toronto-raptors': 'TOR',
    'utah-jazz': 'UTA', 'washington-wizards': 'WAS'
}
result=[]
for team in teamsDictionary.values():
    url =f"https://www.basketball-reference.com/teams/{team}/2022.html"
    html = urlopen(url)

    print(url)

    soup = BeautifulSoup(html, features="lxml")

    table1 = soup.find("table", id="per_game")
    body = table1.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    headings = []
    for item in head.find_all("th"):
        # loop through all th elements
        # convert the th elements to text and strip "\n"
        item = (item.text).rstrip("\n")
        # append the clean column name to headings
        headings.append(item)
    headings.remove("Rk")
    headings[0] = "Player"
    all_rows = [] # will be a list for list for all rows
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"):
            #loop through all row entries
            # row_item.text removes the tags from the entries
            # the following regex is to remove \xa0 and \n and comma from row_item.text
            # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            #append aa to row - note one row entry is being appended
            row.append(aa)
        # append one row to all_rows
        all_rows.append(row)


    df = pd.DataFrame(data=all_rows,columns=headings)
    df = df.assign(Tm=team)
    result.append(df)

result = pd.concat(result)
result.index = np.arange(1, len(result) + 1)
filepath = Path('/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/player_data/players2022/PerGame_2022.csv')
result.to_csv(filepath)
