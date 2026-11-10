import time
parts = [f"Item{i}" for i in range(10000)]
start = time.perf_counter()
text1 = ""
for p in parts:
text1 += p + ","t1 = time.perf_counter() - start
start = time.perf_counter()
text2 = ",".join(parts)
t2 = time.perf_counter() - start
print("+= time :", round(t1, 4), "sec")
print("join time:", round(t2, 4), "sec")
