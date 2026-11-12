import copy
stops = {
    (13.08, 80.27): "Chennai",
    (13.04, 80.23): "T Nagar"
}
good = [[0 for j in range(4)] for i in range(3)]
good[0][1] = 7
a = [1, 2, 3]
b = copy.copy(a)
c = copy.deepcopy(a)
print("Stops:", stops)
print("Grid:", good)
print("Original:", a)
print("Shallow Copy:", b)
print("Deep Copy:", c)
