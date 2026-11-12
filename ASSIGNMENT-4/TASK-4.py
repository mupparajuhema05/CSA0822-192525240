from io import StringIO
try:
    book = input("Enter book name: ")
    student = input("Enter student name: ")
    f = StringIO()
    f.write(book + " - " + student + "\n")
    print("Return details saved successfully!")
    print("File Content:")
    print(f.getvalue())
except Exception as e:
    print("Error:", e)
