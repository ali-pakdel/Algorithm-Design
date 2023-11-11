import math

class SecondProb:
    def __init__(self, dp, l_s, l_t, s, t):
        self.dp = dp
        self.l_s = l_s
        self.l_t = l_t
        self.s = s
        self.t = t
        self.d = dp

    def solve(self):
        flag = 0
        same = []
        l_same = 0
        for i in range(self.l_t):
            if self.t[0] == self.s[i]:
                dp[0][i] = 0
                same.append(i)
                l_same += 1
                flag = 1
        if flag == 0:
            print(-1)
            return
        self.loop(same, l_same, 1)
        
    def loop(self, same, l_same, tt):
        #for i in range (l_same):
        self.rec(same[0], tt, 0)
        mm = 99999
        for i in range (self.l_s):
            if self.dp[self.l_t - 1][i] < mm and self.dp[self.l_t - 1][i] != -1:
                mm = self.dp[self.l_t - 1][i]
        print(mm)
    def rec(self, ss, tt, x):
        same = []
        l_same =0
        
        #if tt <= self.l_t -1:
         #   if dp[tt - 1][ss] == -1:
          #      dp[tt - 1][ss] = x
           # elif dp[tt - 1][ss] > x:
            #    dp[tt - 1][ss] = x
        if tt > self.l_t - 1:
            if dp[tt - 1][ss] == -1:
                dp[tt - 1][ss] = x
            else:
                if dp[tt - 1 ][ss] > x:
                    dp[tt - 1][ss] = x
            mm = 99999
            for i in range (self.l_s):
                if self.dp[self.l_t - 1][i] < mm and self.dp[self.l_t - 1][i] != -1:
                    mm = self.dp[self.l_t - 1][i]
            print(mm)
            exit()
        
        if ss >= 1:
            if self.s[ss - 1] == self.t[tt]:
                self.rec(ss - 1, tt + 1, x+1)

        if ss < self.l_s - 1:
            if self.s[ss + 1] == self.t[tt]:
                self.rec(ss + 1, tt + 1, x+1)

        flag = 0
        for j in range (self.l_s):
            if self.s[j] == self.s[ss] and j != ss:
                if j >= 1 and self.s[j - 1] != self.t[tt]:
                    if j <= self.l_s - 1 and self.s[ss + 1] != self.t[tt]:
                        continue
            if self.s[j] == self.t[tt] and j != ss:
                flag = 1
                if j > ss:
                    x += j - ss
                else:
                    x += ss - j
                self.rec(j, tt + 1, x)
                return
            
        if flag == 0:
            print(-1)
            exit()

def fill_dp(s, t):
    dp = [ [-1]*s for i in range(t)]
    return dp

s, t = list(map(int, input().split()))
str_ss = input(str())
str_tt = input(str())
str_s = list(str_ss)
str_t = list(str_tt)

dp = fill_dp(s, t)
res = SecondProb(dp, s, t, str_s, str_t)
res.solve()
