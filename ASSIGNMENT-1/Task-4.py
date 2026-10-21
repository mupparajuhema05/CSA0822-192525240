import math
fat = 4.2
snf = 8.5
litres = 10
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.0) / 0.1)
rate = 30 + fat_steps * 0.4 + snf_steps * 0.3
amount = litres * rate
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", round(rate, 2))
print("Amount:", round(amount, 2))
print(round((4.2 - 3.5) / 0.1))
print(int(-2.5))
print(math.floor(-2.5))
print(2.0 <= fat <= 7.0)
