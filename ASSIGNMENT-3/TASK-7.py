contacts = [
    {"name": "Ravi", "phone": "+91 98400 12345",
     "email": "ravi@gmail.com"},
    {"name": "Ravi Kumar", "phone": "9840012345",
     "email": "rk@gmail.com"},
    {"name": "Sita", "phone": "9876543210",
     "email": "sita@gmail.com"}
]
merged = {}
for c in contacts:
    phone = "".join(ch for ch in c["phone"] if ch.isdigit())
    if phone not in merged:
        merged[phone] = {
            "name": c["name"],
            "phones": set(),
            "emails": set()
        }
    merged[phone]["phones"].add(phone)
    merged[phone]["emails"].add(c["email"])
for contact in merged.values():
    print(contact)
