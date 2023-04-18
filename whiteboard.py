# Create a function name all_non_consecutive

# E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.

# You should return the results as an array of objects with two values i: <the index of the non-consecutive number> and n: <the non-consecutive number>.

# E.g., for the above array the result should be:

# [
#   {'i': 4, 'n': 6},
#   {'i': 7, 'n': 15}
# ]
# If the whole array is consecutive or has one element then return an empty array.

# The array elements will all be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive and/or negetive and the gap could be larger than one.

# def all_non_consecutive(arr):
#     dict = {}
#     for i in range(len(arr)-1):
#         if arr[i+1] - arr[i] > 1:
#             dict['i'] = i+1
#             dict['n'] = arr[i+1]
#     print(dict)

# array = [1,2,3,4,6,7,8,15,16]

# print(all_non_consecutive(array))

# def fint_non_consec(alist):
#     return [{'i': i, 'n':n} for i, n in enumerate(alist[1:], start=1) if n != alist[i-1]+1]

# with open("files/names.txt")as f:
#     data = f.readlines()
#     print(data[0])

# pattern = re.compile("([A-Z][a-z]+), ([\w -]*)([A-Z][a-z]+).*\s(@[a-zA-Z0-9]+$)")

# for person in data:
#     match = pattern.search(person)
    
#     if match:
#         print('\n', f"{match.group(3)} {match.group(2)}{match.group(1)} / {match.group(4)}")


import re

with open('./regex_test.txt') as f:
    data = f.readlines()
    print(data[0])

pattern = re.compile("([A-Z][a-z]+)([A-Z]*[a-z])([A-Z][a-z]+)")
for each in data:
    match = pattern.match(each)
    if match:
        print(f'{match.group(1)}{match.group(2)}{match.group(3)}')