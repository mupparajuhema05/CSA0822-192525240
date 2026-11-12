calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}
def frequencies(texts):
    counts = {}
    for text in texts:
        for word in text.split():
            if word not in STOP:
                counts[word] = counts.get(word, 0) + 1
    return counts
counts = frequencies(calls)
top = sorted(counts.items(),
             key=lambda x: (-x[1], x[0]))
print("Word Frequencies:", counts)
print("Top Words:", top[:3])
