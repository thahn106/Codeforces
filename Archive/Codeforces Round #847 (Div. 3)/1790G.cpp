#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

int n, m, p, b;
vector<vector<int>> graph;
vector<int> token;
vector<int> bonus;
vector<int> valid;

void input()
{
    cin >> n >> m >> p >> b;
    graph.clear();
    token.clear();
    bonus.clear();
    valid.clear();
    graph.resize(n);
    token.resize(n, 0);
    bonus.resize(n, 0);
    valid.resize(n, 0);
    forn(i, p)
    {
        int t;
        cin >> t;
        token[t - 1] = 1;
    }
    forn(i, b)
    {
        int t;
        cin >> t;
        bonus[t - 1] = 1;
    }
    forn(i, m)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
}

vector<bool> visited;
int bfs(int start)
{
    vector<int> dis(n, 2 * n);
    int mind = 2 * n;
    int ans = 0;
    queue<int> q;
    q.push(start);
    visited[start] = true;
    dis[start] = 0;
    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        for (auto &to : graph[cur])
        {
            if (!visited[to])
            {
                visited[to] = true;
                if (token[to])
                {
                    if (mind > dis[cur] + 1)
                    {
                        mind = dis[cur] + 1;
                        ans = to;
                    }
                }
                if (bonus[to])
                {
                    dis[to] = dis[cur] + 1;
                    q.push(to);
                }
            }
        }
    }
    if (mind == 2 * n)
    {
        return -1;
    }
    else
    {
        token[ans] = mind;
        return ans;
    }
}

void bfs_bonus(int start)
{
    set<int> adj;
    int ans = 0;
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while (!q.empty())
    {
        int cur = q.front();
        ans++;
        q.pop();
        for (auto &to : graph[cur])
        {
            if (token[to])
            {
                adj.insert(to);
            }
            if (!visited[to])
            {
                if (bonus[to])
                {
                    visited[to] = true;
                    q.push(to);
                }
            }
        }
    }
    for (auto &it : adj)
    {
        valid[it] = max(valid[it], ans);
    }
}

void solve()
{
    input();
    int finish = 0;
    if (token[finish])
    {
        cout << "YES\n";
        return;
    }
    visited.clear();
    visited.resize(n, 0);
    int best = bfs(0);
    if (best == -1)
    {
        cout << "NO\n";
        return;
    }
    visited.clear();
    visited.resize(n, 0);
    forn(i, n)
    {
        if (!visited[i] && bonus[i])
        {
            bfs_bonus(i);
        }
    }
    bool ans = false;
    int count = 0;
    int mind = token[best] - 1;
    // cout << "MIND:" << mind << endl;
    forn(i, n)
    {
        if (valid[i] && i != best)
        {
            if (valid[i] > 1)
            {
                ans = true;
                break;
            }
            count += valid[i];
        }
    }
    if (count >= mind)
    {
        ans = true;
    }
    cout << (ans ? "YES\n" : "NO\n");
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
