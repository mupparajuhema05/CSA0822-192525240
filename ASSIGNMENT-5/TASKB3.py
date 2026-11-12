import sqlite3
data = [("Adyar", 48), ("Adyar", 60), ("Guindy", 95)]
total = {}
count = {}
for s, v in data:
    total[s] = total.get(s, 0) + v
    count[s] = count.get(s, 0) + 1
for s in total:
    print(s, total[s] / count[s])
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE air (station TEXT, pm REAL)")
db.executemany("INSERT INTO air VALUES (?, ?)", data)
print(list(db.execute(
    "SELECT station, AVG(pm) FROM air GROUP BY station"
)))
