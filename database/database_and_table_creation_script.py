import sqlite3

conn = sqlite3.connect('fugo_games_case.db')
c = conn.cursor()

# Create table - TV_SHOWS
c.execute('''CREATE TABLE TV_SHOWS
             ([id] INTEGER PRIMARY KEY,[name] text, [overview] text, [number_of_seasons] integer,
             [number_of_episodes] integer, [popularity] float, [vote_average] float,
             [vote_count] integer, [first_air_date] date, [last_air_date] date, [status] text)''')

# Create table - CAST
c.execute('''CREATE TABLE CAST
             ([id] INTEGER PRIMARY KEY,[name] text, [gender] integer,
             [known_for_department] text, [popularity] float)''')

# Create table - CREW
c.execute('''CREATE TABLE CREW
             ([id] INTEGER PRIMARY KEY,[name] text, [gender] integer,
             [known_for_department] text, [popularity] float)''')

# Create table - DIRECTORS
c.execute('''CREATE TABLE DIRECTORS
             ([tv_show_names] text,[episode_count] integer, [director_id] integer PRIMARY KEY)''')


conn.commit()

