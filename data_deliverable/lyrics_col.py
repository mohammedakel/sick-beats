import sqlite3

# Create connection to database
conn = sqlite3.connect('billboard.db')
c = conn.cursor()

lyrics_cmd = '''
ALTER TABLE 
	billboard
ADD
	lyrics text
'''

c.execute(lyrics_cmd)

conn.commit()
c.close()
conn.close()