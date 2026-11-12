trains = {
    "101": {
        "name": "Express",
        "stations": [
            ("Chennai", "08:00", "08:10"),
            ("Vellore", "10:00", "10:05")
        ],
        "days": {"Monday", "Tuesday"}
    },
    "102": {
        "name": "Superfast",
        "stations": [
            ("Chennai", "09:00", "09:10"),
            ("Vellore", "11:00", "11:05")
        ],
        "days": {"Monday", "Friday"}
    }
}
for number, details in trains.items():
    if "Monday" in details["days"]:
        for station, arrival, departure in details["stations"]:
            if station == "Vellore":
                print(number, details["name"],
                      station, arrival, departure)
