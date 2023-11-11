class Trip:
    def __init__(self, n, k, dis, lit):
        self.n = n
        self.k = k
        self.dis = dis
        self.lit = lit
        self.v = lit[0]
        self.wait = 0
        self.cur = 0
        self.best = 0

    def solve(self, s):
        while self.cur < self.n:
            flag = 0
            if self.cur > 0 and self.cur < self.n and self.lit[self.cur] > self.lit[self.best]:
                self.best = self.cur
            if self.v >= self.dis[self.cur]:
                flag = 1
                self.cur += 1
                if self.cur < self.n:
                    self.v -= self.dis[self.cur-1]
                    self.v += self.lit[self.cur]
            if flag == 0:
                temp = ((self.dis[self.cur] - self.v) // self.lit[self.best]) + 1
                self.wait += temp
                self.v += temp * self.lit[self.best]
                self.v -= self.dis[self.cur]
                self.cur += 1
                if self.cur < self.n:
                    self.v += self.lit[self.cur] 

        
        print(s + ((self.k * self.wait)))

    #def wait_needed(self):
     #   if self.v < self.dis[self.cur]:
      #      temp = ((self.dis[self.cur] - self.v) // self.lit[self.cur]) + 1
       #     self.wait += temp
        #    self.v += temp * self.lit[self.cur]
            
    #def move_next(self):
     #   self.wait_needed(self):
      #  if self.lit[self.cur] <= self.lit[self.cur + 1]:
       #     self.v -= self.dis[cur]
        #    self.cur += 1
         #   return true
        #return false
        
n, k = list(map(int, input().split()))
dis = list(map(int, input().split()))
lit = list(map(int, input().split()))
s = 0
for i in range (n):
    s += dis[i]
trip = Trip(n, k, dis, lit)
trip.solve(s)
