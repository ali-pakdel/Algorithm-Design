class Table:
    def __init__(self, n):
        self.n = n
        
        self.ws = []
        temp = [0] * (n + 2)  
        self.residual = [ temp * 1 for _ in range(n + 2) ]
        #self.residual = [[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0], [0, 0, 9, 0, 0, 20], [0, 0, 0, 7, 0 , 4], [0, 0, 0, 0, 0, 0]]
        #self.residual = [[0, 5, 2, 6, 0, 0, 0, 0], [0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0], [0, 0, 0, 0, 0, 3, 0, 8], [0, 0, 0, 0, 0, 0, 7, 8], [0, 0, 3, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0]]        
        self.weights = [ temp * 1 for _ in range(n + 2) ]
        self.edges_flow = [ temp * 1 for _ in range(n + 2) ]

        for i in range (1, n//2 + 1):
           self.residual[0][i] = 1

        self.parent = [-1] * (n + 2)
        #print(self.residual)
        
        for i in range(n//2 + 1, n + 1):
            self.residual[i][n + 1] = 1
            
        #self.out_nodes = temp1 + [ [0]*1 for _ in range(n + 1) ]
        #self.in_nodes = temp2 + [ [0]*1 for _ in range(n + 1) ]
        
        self.nodes_flow = [-1] * (n + 2)

        self.res = 0
        self.ress = []

    def add_w(self, u, v, w):
        self.residual[u][v] = 1
        self.weights[u][v] = w

    def dfs(self, v, flow):
        self.nodes_flow[v] = flow

        if v == 0:
            for i in range (1, (self.n // 2) + 1):
                if self.nodes_flow[i] == -1 and self.residual[v][i] - self.edges_flow[v][i] > 0:
                    self.parent[i] = v
                    dfs(i, min(flow, self.residual[v][i] - self.edges_flow[v][i]))

            for i in range (1, (self.n // 2) + 1):
                if self.nodes_flow[i] == -1 and self.edges_flow[i][v] > 0:
                    self.parent[i] = v
                    dfs(i, min(flow, self.edges_flow[i][v]))
                    
        elif v == n + 2:
            for i in range ((self.n // 2) + 1, self.n + 2):
                if self.nodes_flow[i] == -1 and self.residual[v][i] - self.edges_flow[v][i] > 0:
                    self.parent[i] = v
                    dfs(i, min(flow, self.residual[v][i] - self.edges_flow[v][i]))

            for i in range ((self.n // 2) + 1, self.n + 2):
                if self.nodes_flow[i] == -1 and self.edges_flow[i][v] > 0:
                    self.parent[i] = v
                    dfs(i, min(flow, self.edges_flow[i][v]))

        
    def bfs(self, src, des, mini):
        self.parent[src] = -1

        vis = [0] * (self.n + 2)
        vis[src] = 1
        
        queue = [src]
        l_q = 1

        while (l_q > 0):
            v = queue.pop()
            l_q -= 1

            i = 0
            while i < self.n + 2:
                if vis[i] == 0:
                    #print(v, i)
                    if self.residual[v][i] > 0:
                        #print(self.residual)
                        #print(mini, self.residual[v][i])
                        if self.weights[v][i] <= mini: 
                            if i == des:
                                #print(v, self.parent)
                                self.parent[i] = v

                                #print("x",i, des, self.parent)
                                return 1
                            queue.append(i)
                            l_q += 1
                            self.parent[i] = v
                            vis[i] = 1
                #print(v, i, self.parent)
                i += 1
        return 0

    def add_ws(self, a):
        self.ws += a
            
    def ford(self, mini):
        flow = 0

        while (True):
            #print(self.residual)
            n_flow = self.bfs(0, self.n + 1, mini)
            if n_flow == 0:
                break

            flo = self.find_flow()
            self.res += flo
            self.update_res(flo)
            #print("FFF", flo)

        
        #print(self.res)
        #print(self.ress)

    def update_res(self, flo):
        i = self.n + 1
        while i != 0:
            x = self.parent[i]
            self.residual[x][i] -= flo
            self.residual[i][x] += flo
            i = x

    def find_flow(self):
        flo = 9999999999
        i = self.n + 1
        #print(i, self.parent)
        while i != 0:
            x = self.parent[i]
            flo = min(flo, self.residual[x][i])
            #print("xx", x, i, flo)
            if x != 0 and x != self.n + 1 and i != 0 and i != self.n + 1:
                self.ress.append(self.weights[x][i])
            i = x
        return flo

    def solve(self):
        self.ws.sort()

        for i in self.ws:
            self.ford(i)
            #print("mini ", i)
            if self.res == self.n // 2:
                print(i)#
                break
            self.ress = []


        #self.printt()


    def printt(self):
        #print(self.out_nodes)
        #print(self.in_nodes)

        print(self.residual)
        print(self.weights)
        print(self.nodes_flow)
        print(self.ws)
        


nn = input()
n = int(nn)
table = Table(2 * n)
table.solve()

for i in range (1, n + 1):
    row = list(map(int, input().split()))
    table.add_ws(row)
    for j in range (n + 1, (2 * n) + 1):
        table.add_w(i, j, row[j - n - 1])

table.solve()
