class InvalidMarkError(Exception):
    pass
try:
    mark = int(input("Enter student marks: "))
    if mark < 0 or mark > 100:
        raise InvalidMarkError("Invalid marks!")
except ValueError:
    print("Please enter numbers only.")
except InvalidMarkError as e:
    print(e)
else:
    print("Valid Marks:", mark)
finally:
    print("Program Completed")
