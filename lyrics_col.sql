import sqlite3

# Create connection to database

conn = sqlite3.connect('billboard.db')
c = conn.cursor()

alter_cmd = '''
	ALTER TABLE billboard
    ADD lyrics TEXT
'''
c.execute(alter_cmd)

c.commit()
c.close()
conn.close()