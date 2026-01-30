n = 100
print(n)

# Hospitals: i, i+1, ..., n, 1, ..., i-1
for i in range(1, n + 1):
    prefs = list(range(i, n + 1)) + list(range(1, i))
    print(" ".join(map(str, prefs)))

# Students: i, i-1, ..., 1, n, n-1, ..., i+1
for i in range(1, n + 1):
    prefs = list(range(i, 0, -1)) + list(range(n, i, -1))
    print(" ".join(map(str, prefs)))
    