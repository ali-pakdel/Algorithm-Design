class Iran:
    def __init__(self, n, m, popu):
        self.edges = []
        self.n = n
        self.m = m
        self.popu = popu
        
        self.mst = []
        self.mst_l = 0

        self.sum = 0

        self.deg = [1] * (n + 1)
        
        self.p = []
        for i in range (0, n+1):
            self.p.append(i)

        self.h = [0] * (n + 1)

    def add_edge(self, u, v):
        w1 = self.popu[v - 1]
        w2 = self.popu[u - 1]
        w = w1
        if w1 > w2:
            w = w2
        self.edges.append((u, v, w))

    def find(self, v):
        while self.p[v] != v:
            v = self.p[v]
        return v
    
    def union(self, u, v):
        r1 = self.find(u)
        r2 = self.find(v)
        
        #print("U", u, r1)
        #print("V", v, r2)
            
        if self.h[r1] > self.h[r2]:
            self.p[r2] = r1
            self.deg[r1] += self.deg[r2]
            
        elif self.h[r1] < self.h[r2]:
            self.p[r1] = r2
            self.deg[r2] += self.deg[r1]

        elif self.h[r1] == self.h[r2]:
            self.p[r2] = r1
            self.h[r1] += 1
            self.deg[r1] += self.deg[r2]

        #print("New U", u, self.p[r1])
        #print("New V", v, self.p[r2])

        #x1 = self.find(u)
        #x2 = self.find(v)
        #print("DEEG",self.deg[x1] , self.deg[x2])

    def kruskal(self):
        self.edges.sort(key=lambda x:x[2], reverse=True)
        #print(self.edges)
        y = 0
        for i in range(self.m):
            u = self.edges[i][0]
            v = self.edges[i][1]
            w = self.edges[i][2]

            r_u = self.find(u)
            r_v = self.find(v)


            #print("U", u , r_u)
            #print("V", v, r_v)

            deg1 = self.deg[r_u]
            deg2 = self.deg[r_v]
            
            if r_u != r_v:
                #self.mst.append((u, v, w))
                self.mst_l += 1
                self.union(r_u, r_v)

                y += 1
                x = deg1 * deg2
                self.sum += x * w
                #print(deg1, deg2)
                #print(deg1, "* " , deg2 , " * " , w)

            #print("P U", u, self.p[u])
            #print("P V", v, self.p[v])

            #print(self.mst)
            if self.mst_l == n - 1:
                break;
        #print(self.mst)
        #print(self.p)
        print(self.sum)

n, m = list(map(int, input().split()))
popu = list(map(int, input().split()))
iran = Iran(n ,m, popu)

for i in range (m):
    u, v = list(map(int, input().split()))
    iran.add_edge(u, v)

iran.kruskal()
