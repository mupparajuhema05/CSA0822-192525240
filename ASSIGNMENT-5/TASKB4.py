positive = ["good", "clean", "helpful"]
negative = ["bad", "dirty", "smoke"]
text = input("Enter complaint: ").lower()
score = 0
for word in text.split():
    if word in positive:
        score += 1
    elif word in negative:
        score -= 1
if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Neutral")
