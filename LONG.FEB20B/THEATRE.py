"""
@author Vivek
@since 14/02/20
"""


class Local:

    def __init__(self, count, row):
        self.c = count
        self.r = row

    def __eq__(self, other):
        return self.c != other.m

    def __hash__(self):
        return hash(self.c)

    def __repr__(self):
        return "{} : {}".format(self.c, self.r)


t = int(input())
total_cost = 0
while t > 0:
    n = int(input())
    # data = [[0] * 13] * 4  # col x row -- shallow list
    data = [[0 for i in range(13)] for j in range(4)]
    while n > 0:
        val = input().split(' ')
        row = ord(val[0]) - 65
        data[row][int(val[1])] += 1
        n -= 1
    cost = 0
    done = set()  # movies
    prices = [100, 75, 50, 25]
    [print(val) for val in data]
    for j in range(3, 13, 3):
        inc = []
        for i in range(0, 4): inc.append(Local(data[i][j], i))
        inc.sort(key=lambda x: x.c, reverse=True)
        print(inc)
        for val in inc:
            if val.r not in done:
                done.add(val.r)
                if val.c == 0:
                    cost -= 100
                    continue
                cost += val.c * prices[0]
                print('new cost : '+str(cost))
                prices.pop(0)
    print(cost)
    total_cost += cost
    t -= 1
    break
print(total_cost)
