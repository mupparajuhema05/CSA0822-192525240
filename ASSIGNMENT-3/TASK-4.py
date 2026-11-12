ai = {"101", "102", "103", "104"}
iot = {"102", "104", "105", "106"}
all_students = {"101", "102", "103",
                "104", "105", "106", "107"}
both = ai & iot
exactly_one = ai ^ iot
neither = all_students - (ai | iot)
print("Clash:", sorted(both))
print("Exactly One:", sorted(exactly_one))
print("Neither:", sorted(neither))
