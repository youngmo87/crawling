import random
from pprint import pprint
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}


class Diff_sum:    
    def __init__(self):
        self.list_result = []
        self.name=i

    def testing(self):
        for i in range(0,5):
            k = data[self.name][i][i]
            self.list_result.append(k)
            data[self.name][i].reverse()
            k = data[self.name][i][i]
            self.list_result.append(k)

list_dict = []
Result = {}

for key in data.keys():
    list_dict.append(key)

for i in list_dict:
    i = Diff_sum()
    i.testing()
    Result[i.name] = sum(i.list_result)
    minResult = sorted(Result.items(), key=lambda x : x[1])
    
print(Result)
print(minResult[0][0])
