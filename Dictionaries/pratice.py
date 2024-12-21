arr = "python is a great language"


Frequency_map = dict()
n = len(arr)
for i in range(n):
    Frequency_map[arr[i]] = Frequency_map.get(arr[i], 0) + 1

print(Frequency_map)

"""
Frequency_map = dict()
n = len(arr)
for i in range(n):
    if arr[i] in Frequency_map:
        Frequency_map[arr[i]] = Frequency_map[arr[i]] + 1
    else:
        Frequency_map[arr[i]] = 1

print(Frequency_map)
"""
