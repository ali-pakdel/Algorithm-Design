#include <iostream>
#include <vector>

using namespace std;

class Jazab
{
public:
	Jazab(long long int n_, long long int m_);
	void add_edge(long long int a, long long int b, long long int w);
	void add_rule(long long int u, long long int v, long long int l);
	void solve();
	//void print()
	//{
	//	for (long long int i = 1; i < n + 1; i++)
	//	{
	//		for (long long int j = 1; j < g[i].size(); j++)
	//			cout <<"V  " <<i << " " << g[i][j].second << " " << g[i][j].first << endl;
	//	}

	//	cout << endl << endl;

	//	for (long long int i = 0; i < rules.size() ; i++)
	//	{
	//		for (long long int j = 0; j < rules[i].size(); j++)
	//			cout << rules[i][j] << " ";
	//		cout << endl;
	//	}

	//}


	void floyd_warshall();
	void check_edges();
	void check_max();

private:
	long long int n;
	long long int m;
	long long int no_rules = 0;

	vector<vector<long long int>> rules;
	vector<vector<long long int>> g;
	vector<vector<long long int>> weights;
	vector<vector<long long int>> fw;
	vector<vector<long long int>> jazabs;

	long long int res = 0;
};

Jazab::Jazab(long long int n_, long long int m_)
{
	n = n_;
	m = m_;

	vector<long long int> temp{0};
	vector<vector<long long int>> a(n_ + 1, temp);
	g = a;

	vector<long long int> temp2(n_ + 1, -1);
	vector<vector<long long int>> ed(n_ + 1, temp2);
	weights = ed;


	vector<long  long int> f1(n_ + 1, 999999999999);
	vector<vector<long long int>> fwt(n_ + 1, f1);

	fw = fwt;

	vector<vector<long long int>> jzbs(n_ + 1, temp2);

	jazabs = jzbs;
}

void Jazab::add_edge(long long int a, long long int b, long long int w)
{
	g[a].push_back(b);
	g[a][0]++;
	fw[a][b]= w;
	fw[b][a] = w;

	weights[a][b] = w;
	weights[b][a] = w;
}

void Jazab::add_rule(long long int u, long long int v, long long int l)
{
	vector<long long int> temp{u, v, l};
	rules.push_back(temp);
	no_rules++;
}

void Jazab::floyd_warshall()
{
	for (long long int i = 1; i < n + 1; i++)
	{
		fw[i][i] = 0;
		weights[i][i] = 0;
	}

	for (long long int k = 1; k < n + 1; k++)
		for (long long int i = 1; i < n + 1; i++)
			for (long long int j = 1; j < n + 1; j++)
			{
				if (fw[i][j] > fw[i][k] + fw[k][j])
					fw[i][j] = fw[i][k] + fw[k][j];
			}

	//	for (long long int i = 1; i < n + 1; i++)
	//	for (long long int j = 1; j < n + 1; j++)
	//		cout << i << "  " << j << "   dis: " << fw[i][j] << endl;
}

void Jazab::check_edges()
{
	for (long long int k = 0; k < no_rules; k++)
	{
		long long int u = rules[k][0];
		long long int v = rules[k][1];
		long long int l = rules[k][2];
		jazabs[u][v] = jazabs[v][u] = l;
	}
}

void Jazab::check_max()
{
	for (long long int s = 1 ; s < n + 1; s++)
		for (long long int l = 1; l < n + 1; l++)
			for (long long int m = 1; m < n + 1; m++)
			{
				jazabs[s][l] = (jazabs[l][m] <= jazabs[l][s] + fw[s][m]) ? jazabs[l][s] : jazabs[l][m] - fw[s][m];
				jazabs[l][s] = (jazabs[l][m] <= jazabs[l][s] + fw[s][m]) ? jazabs[l][s] : jazabs[l][m] - fw[s][m];
			}
}

void Jazab::solve()
{
	check_edges();
	check_max();

	for (long long int u = 1; u < n + 1; u++)
		for (long long int v = u + 1; v < n + 1; v++)
		{	
			if (weights[u][v] != -1)
				res = (jazabs[u][v] >= weights[u][v]) ? res + 1 : res;
		}

	cout << res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	long long int n, m, a, b, w, k, u, v, l;

	cin >> n >> m;
	Jazab jazab = Jazab(n, m);

	for (long long int i = 0; i < m; i++)
	{
		cin >> a >> b >> w;
		jazab.add_edge(a, b, w);
	}
	
	cin >> k;

	for (long long int i = 0; i < k; i++)
	{
		cin >> u >> v >> l;
		jazab.add_rule(u, v, l);
	}
	jazab.floyd_warshall();
	jazab.solve();
	//jazab.print();
}

//5 7
//1 2 1
//2 3 1
//3 4 1
//1 3 3
//2 4 3
//1 4 5
//1 5 2
//1
//1 4 4
