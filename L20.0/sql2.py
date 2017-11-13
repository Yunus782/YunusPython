import sqlite3

big_data_db = sqlite3.connect("hot_countries.db")
runner = big_data_db.cursor()


runner.execute("SELECT * FROM our_hot_countries")
countries = runner.fetchall()
print(countries)

runner.execute("SELECT name, capital FROM our_hot_countries WHERE population > 100000000 ORDER BY population DESC LIMIT 1")
countries2 = runner.fetchall()
print(countries2)

	
big_data_db.commit()

runner.close()
big_data_db.close()