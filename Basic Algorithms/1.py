import sys
sys.setrecursionlimit(100000)
class MinPaints:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        
    def find_min_ways(self, first, last, min_height):
        if last < first:
            return 0
        if last == first:
            return 0
        
        min_index = first
        for i in range(first, last):
            if self.a[min_index] > self.a[i]:
                min_index = i
        
        res_left = self.find_min_ways(first, min_index, self.a[min_index])
        res_right = self.find_min_ways(min_index + 1, last, self.a[min_index])
        horiz_ways = self.a[min_index] - min_height

        vertical_ways = last - first

        if res_left + res_right + horiz_ways >= vertical_ways:
            return vertical_ways
        else:
            return res_left + res_right + horiz_ways
        

n = int(input())
a = list(map(int,input().split()))
if n == 1:
    print("1")
else:
    res = MinPaints(n, a)
    print(res.find_min_ways(0, n, 0))


