def total_bills(filename):
    total = 0
    rejected = []
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 3:
                        raise ValueError("Invalid line")
                    total += float(parts[2])
                except ValueError:
                    rejected.append(line.strip())
        print("Total:", total)
        print("Rejected:", rejected)
    except FileNotFoundError:
        print("File not found")
total_bills("mess_oct.txt")
