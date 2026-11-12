readings = [5, 10, 55, -60, 7, 3, 45]
valid = [x for x in readings if -50 <= x <= 50]
fahrenheit = [(x * 9/5) + 32 for x in valid]
alarms = [i for i, x in enumerate(readings)
          if x < 2 or x > 8]
print("Valid Readings:", valid)
print("Fahrenheit:", fahrenheit)
print("Alarm Minutes:", alarms)
