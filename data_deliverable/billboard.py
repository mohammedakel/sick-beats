from bs4 import BeautifulSoup
import requests
import sqlite3

### BILLBOARD SCRAPING
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

# Use BeautifulSoup and requests to collect data required for the assignment.
r = requests.get(BILLBOARD_URL).text
soup = BeautifulSoup(r, 'html.parser')
post = soup.find(id='post-1479786')
pmc = post.find('div', 'pmc-paywall')
layer1 = pmc.find('div')
layer2 = layer1.find('div')
layer3 = layer2.find('div')
chart = layer3.find('div', 'chart-results-list')
row_containers = chart.find_all('div', 'o-chart-results-list-row-container')

rows = []
for row_container in row_containers:
    rows.append(row_container.find('ul'))

data = []
for row in rows:
    pos_wrap = row.find('li')

    rest_wrap1 = row.find('li', 'lrv-u-width-100p')
    rest_wrap2 = rest_wrap1.find('ul')
    rest = rest_wrap2.find_all('li')

    # get song ranking
    pos = int(pos_wrap.find('span').string.strip())
    # get song title
    title = rest[0].find('h3').string.strip()
    # get song artist
    artists = rest[0].find('span').string.strip()
    r = artists.replace(' &', ',').replace(' /', ',').replace(' X ', ', ')
    r2 = r.replace(' (', ', ').replace(' Featuring', ',')
    names = r2.split(', ')
    if names[-1][-1] == ")":
        names[-1] = names[-1][:-1]
    # get last week ranking
    prev_pos = rest[3].find('span').string.strip()
    if prev_pos == '-':
        prev_pos = None
    else:
        prev_pos = int(prev_pos)
    # get peak ranking
    peak_pos = int(rest[4].find('span').string.strip())
    # get weeks on chart
    weeks = int(rest[5].find('span').string.strip())

    data.append({
        'pos': pos,
        'title': title,
        'artists': names,
        'prev_pos': prev_pos,
        'peak_pos': peak_pos,
        'weeks': weeks
    })

# Create connection to database
conn = sqlite3.connect('billboard.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "billboard";')

# Create tables in the database and add data to it.
# use CREATE TABLE to create the companies table in the database
create_billboard_table_command = '''
CREATE TABLE IF NOT EXISTS billboard (
    rank REAL,
    title VARCHAR NOT NULL,
    artist VARCHAR NOT NULL,
    prev_rank REAL,
    peak_rank REAL,
    weeks REAL,
    PRIMARY KEY (title, artist)
);
'''
c.execute(create_billboard_table_command)

# use INSERT to add data to the tables in the database
for idx in range(len(data)):
    # initialize the rank value
    r = data[idx]['pos']
    # initialize the title value
    t = data[idx]['title']
    # initialize the artist value (only the first artist)
    a = data[idx]['artists'][0]
    # initialize the prev_rank value
    pv = data[idx]['prev_pos']
    # initialize the peak_rank value
    pk = data[idx]['peak_pos']
    # initialize the weeks value
    w = data[idx]['weeks']

    c.execute('INSERT INTO billboard VALUES (?, ?, ?, ?, ?, ?)', (r, t, a, pv, pk, w))

conn.commit()