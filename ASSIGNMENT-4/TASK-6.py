students = set()
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ").strip()
    if name:
        students.add(name)
print("\nFinal Registration List:")
for name in sorted(students):
    print(name)
print("Total Registrations:", len(students))
