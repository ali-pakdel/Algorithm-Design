class Tree:
    def __init__(self, n):
        self.n = n
        temp = [ [1]*1 for _ in range(n + 1) ]
        self.nei = temp
        self.ans = 0
        
        self.lvs = []
        self.ls = 0

        self.flag = 0
        
    def add_ver(self, u, v):
        self.nei[u].append(v)
        self.nei[u][0] += 1
        self.nei[v].append(u)
        self.nei[v][0] += 1

        if self.nei[u][0] > 2 or self.nei[v][0] > 2:
            self.flag = 1

    def find_lvs(self, u, v):
        for i in range(1, self.n + 1):
            if self.nei[i][0] == 2 and i != u and i != v:
                self.lvs.append(i)
                self.ls += 1

    def find_leaf(self):
        for i in range(1, self.n + 1):
            if self.nei[i][0] == 2:
                return i

    def solve(self):
        if self.flag == 0:
            i = self.find_leaf()
            b = self.find_node(i)
            jvb = b[self.lvs[1]]
            print(((jvb*(jvb +1))//2))
            
        else:
            m = self.find_longest_path()
            print(self.ans+ ((m*(m+1))//2))

    def find_longest_path(self):
        #rishe
        #x = self.find_root()
            
        starts = self.find_node(1)
                
        src = self.find_node(starts[n+1])

        des = self.find_node(src[n+1])

        self.find_lvs(starts[n+1], src[n+1])
        #print(self.lvs)
        #print("S", idx1)
        #print("E", idx2)
        #print("DIA", m)
        
        while self.ls > 0:
            a = src[self.lvs[0]]
            b = des[self.lvs[0]]
            if a > b:
                self.ans += a
            else:
                self.ans += b
            #print("ANS", self.ans)
            self.delete_node(self.lvs[0])
        return src[0]

    def find_root(self):
        i = 1
        m = 0
        idx = 0
        while i < n + 1:
            if m < self.nei[i][0]:
                m = self.nei[i][0]
                idx = i
            i += 1
        return idx
    
    def delete_node(self, node):
        self.lvs.pop(0)
        self.ls -= 1

        #print(node)
        #   print(self.nei)
        self.nei[self.nei[node][1]].remove(node)
        self.nei[self.nei[node][1]][0] -= 1
        
        if self.nei[self.nei[node][1]][0] == 2:
            self.lvs.append(self.nei[node][1])
            self.ls += 1

    def find_node(self, v1):
        vis = [0] * (self.n+1)
        dis = [0] * (self.n+1)
        vis[v1] = 1
        lis = [v1]
        l = 1
        m = 0
        idx = 0
        while l > 0:
            v2 = lis[0]
            lis.pop(0)
            if dis[v2] > m:
                m = dis[v2]
                idx = v2
            l -= 1
            i = 1
            while i < self.nei[v2][0]:
                if vis[self.nei[v2][i]] == 0:
                    vis[self.nei[v2][i]] = 1
                    lis.append(self.nei[v2][i])
                    l += 1
                    dis[self.nei[v2][i]] += dis[v2] + 1
                i += 1

        dis[0] = m
        dis.append(idx)
        return dis

    #t
    def find_max_bros(self, dis):
        idx = 0
        m = 0
        bros = []
        
        for i in range (1,n + 1):
            if dis[i] > m:
                m = dis[i]
                idx = i
                
            elif dis[i] == m and m != 0:
                if self.nei[self.nei[i][1]][0] > self.nei[self.nei[idx][1]][0]:
                    idx = i
                elif self.nei[self.nei[i][1]][0] == self.nei[self.nei[idx][1]][0] and i != idx and self.nei[self.nei[idx][1]][0] == 3:
                    if self.nei[self.nei[i][1]][1] == i:
                        pp1 = self.nei[self.nei[i][1]][2]
                    else:
                        pp1 = self.nei[self.nei[i][1]][1]

                    if self.nei[self.nei[idx][1]][1] == idx:
                        pp2 = self.nei[self.nei[idx][1]][2]
                    else:
                        pp2 = self.nei[self.nei[idx][1]][2]

                    if pp1 > pp2:
                        idx = i
        j = 1
        while j in range (self.nei[self.nei[idx][1]][0]):
            if dis[self.nei[self.nei[idx][1]][j]] == dis[idx]:
                bros.append(self.nei[self.nei[idx][1]][j])
            j += 1
                                 
        bros.insert(0, m)
        #print("B",bros)
        return bros

n = int(input())
tree = Tree(n)
if n==1:
    print(0)
elif n== 2:
    print(1)
    
else:
    for i in range (n - 1):
        u, v = list(map(int, input().split()))
        tree.add_ver(u, v)

    tree.solve()
