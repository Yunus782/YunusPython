import sqlite3

big_data_db = sqlite3.connect("hot_countries.db")
runner = big_data_db.cursor()

runner.execute("DROP TABLE our_hot_countries")

runner.execute("""CREATE TABLE our_hot_countries (
	name VARCHAR(20) PRIMARY KEY, 
	population INT,
	capital VARCHAR(20),
	language VARCHAR(20),
	religion VARCHAR(20)
)""")

runner.execute("INSERT INTO our_hot_countries VALUES('Россия', 145000000, 'Москва', 'русский', 'православие')")
runner.execute("INSERT INTO our_hot_countries VALUES(?, ?, ?, ?, ?)", ('США', 325000000, 'Вашингтон', 'английский', 'протестантизм'))

ins = "INSERT INTO our_hot_countries VALUES(?, ?, ?, ?, ?)"
data = "Сев. Корея", 25000000, "Пхеньян", "корейский", "атеизм"
runner.execute(ins, data)

	
big_data_db.commit()

runner.close()
big_data_db.close()