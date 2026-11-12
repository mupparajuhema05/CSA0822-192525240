attendance = {}
n = int(input("Enter number of records: "))
for i in range(n):
    reg = input("Enter register number: ")
    status = input("Enter attendance (P/A): ").upper()
    if status != "P" and status != "A":
        print("Invalid attendance")
        continue
    if reg not in attendance:
        attendance[reg] = [0, 0]
    attendance[reg][1] += 1
    if status == "P":
        attendance[reg][0] += 1
print("\nAttendance Report")
for reg, data in attendance.items():
    present = data[0]
    total = data[1]
    percentage = (present / total) * 100
    print(reg, ":", round(percentage, 2), "%")
    if percentage < 75:
        print("Low Attendance")
