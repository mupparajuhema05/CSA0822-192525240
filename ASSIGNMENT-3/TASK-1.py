rainfall = [10, 20, 0, 15, 25, 30, 5,
            12, 18, 0, 22, 16, 14, 8]
for i in range(0, len(rainfall), 7):
    print("Weekly Total:", sum(rainfall[i:i+7]))
print("Maximum:", max(rainfall))
print("Minimum:", min(rainfall))
avg = sum(rainfall[:7]) / 7
print("7-Day Average:", avg)
dry_days = [i+1 for i, x in enumerate(rainfall) if x == 0]
print("Dry Days:", dry_days)
