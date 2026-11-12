values = ["48", "NA", "60", "", "-5", "95"]
clean = [float(x) for x in values
         if x not in ("", "NA") and 0 <= float(x) <= 999]
low, high = min(clean), max(clean)
normal = [(x-low)/(high-low) for x in clean]
print("Clean Data:", clean)
print("Normalised:", normal)
