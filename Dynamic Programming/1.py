import math

class FirstProb:
    def __init__(self, table, row, col, k):
        self.table = table
        self.row = row
        self.col = col
        self.k = k

    def find_sides(self, surface):
        sides = []
        for j in range (surface, surface + 20):
            temp = [1, j]
            sides.append(temp)
            x = int(math.sqrt(j))
            for i in range(2, x + 1):
                if j % i == 0:
                    temp = [i, j // i]
                    sides.append(temp)
        print(sides)
        return sides
            
    def fill_dp(self):
        dp = [ [0]*self.col for i in range(self.row)]
        dp[0][0] = self.table[0][0]
        
        for i in range (1, self.row):
            dp[i][0] = dp[i - 1][0] + self.table[i][0]
            
        for j in range (1, self.col):
            dp[0][j] = dp[0][j - 1] + self.table[0][j]
            
        for i in range (1, self.row):
            for j in range (1, self.col):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + self.table[i][j] - dp[i - 1][j - 1]
        return dp


    def rect(self, dp, x, y):
        m = 9999999999
        if x > self.row or y > self.col:
            return 9999999998
        
        for i in range(x - 1, self.row):
            for j in range(y - 1, self.col):
                s = dp[i][j]

                if i - x >= 0 and j - y >= 0:
                    s += dp[i - x][j - y]

                if i - x >= 0:
                    s -= dp[i - x][j]

                if j - y >= 0:
                    s -= dp[i][j - y]

                if s < m:
                    m = s
        return m

    def square(self, dp):
        a = int(math.sqrt(self.k)) + 1
        m = 9999999999
        for i in range(a - 1, self.row):
            for j in range(a - 1, self.col):
                s = dp[i][j]
                
                if i - a >= 0 and j - a >= 0:
                    s += dp[i - a][j - a]
                    
                if i - a >= 0:
                    s -= dp[i - a][j]
                if j - a >= 0:
                    s -= dp[i][j - a]
                    
                if s < m:
                    m = s
        return m
    
    def find_min_sum(self):
        dp = self.fill_dp()
        sides = self.find_sides(self.k)
        l = len(sides)
        m = 9999999999
        for i in range (l):
            m1 = self.rect(dp, sides[i][0], sides[i][1])
            m2 = self.rect(dp, sides[i][1], sides[i][0])
            if m1 < m2:
                if m1 < m:
                    m = m1
            else:
                if m2 < m:
                    m = m2

        if int(math.sqrt(self.k)) * int(math.sqrt(self.k)) != self.k:
            m3 = self.square(dp)
            if m3 < m:
                m = m3
        print(m)

n, m, k = list(map(int, input().split()))

table = []
for i in range (n):
    temp = list(map(int, input().split()))
    table.append(temp)

min_sum = FirstProb(table, n, m, k)
min_sum.find_min_sum()

