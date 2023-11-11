class River:
    def __init__(self, w, l, a):
        self.w = w
        self.l = l
        self.a = a

    def find_min_stones(self, curr, min_sum):
        curr_sum = min_sum
        for i in range(curr, self.w - 1):
            curr_sum += self.a[i]
            curr_sum -= self.a[i - l]
            
            if curr_sum < min_sum:
                min_sum = curr_sum
        return min_sum

w, l = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0;

for i in range(0, l):
    s += a[i]

res = River(w, l, a)
print(res.find_min_stones(l ,s))
