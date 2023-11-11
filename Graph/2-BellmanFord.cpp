#include <iostream>
#include <vector>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	long long int n, m, u, v, w;

	cin >> n >> m;

	vector<vector<long long int>> edges{{0, 0, 0}};
	vector<long long int> dis(n + 1, 999999999999);
	dis[1] = 0;

	for (long long int i = 0; i < m; i++)
	{
		cin >> u >> v;
		vector<long long int> temp{u, v, 2};
		edges.push_back(temp);
		temp[0] = v;
		temp[1] = u;
		temp[2] = -1;
		edges.push_back(temp);
	}
	m = m * 2;

	for (int i = 1; i < n; i++)
		for (int j = 1; j < m + 1; j++)
		{
			u = edges[j][0];
			v = edges[j][1];
			w = edges[j][2];
			
			if (dis[u] + w < dis[v])
				dis[v] = dis[u] + w;
		}

	for (int i = 1; i < m + 1; i++)
	{
		u = edges[i][0];
		v = edges[i][1];
		w = edges[i][2];

		if (dis[u] + w < dis[v])
		{
			cout << "No";
			return 0;
		}
	}
	cout << "Yes";
	return 0;
}