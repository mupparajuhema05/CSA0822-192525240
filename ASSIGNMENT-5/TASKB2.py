import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE air (station TEXT, pm25 REAL)")
data = [("Adyar", 48), ("Guindy", 95), ("Adyar", 60)]
db.executemany("INSERT INTO air VALUES (?, ?)", data)
name = input("Enter station: ")
result = db.execute(
    "SELECT AVG(pm25) FROM air WHERE station=?", (name,)
).fetchone()
print("Average:", result[0])
db.close()
