#include <bits/stdc++.h>
using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)

const int MAXN = 210000;

int ans;
int ME = 1e9;
bool col[MAXN];
int dis[MAXN];
int sources[MAXN];
int lasts[MAXN];
vector<int> edges[MAXN];

void dfs(int start)
{

    int i = 0;
    sources[i] = start;
    lasts[i] = -1;
    i++;
    while (i)
    {
        i--;
        int source = sources[i];
        int last = lasts[i];
        if (col[source])
        {
            ans = min(ans, dis[source]);
        }
        for (auto to : edges[source])
        {
            if (to == last)
            {
                continue;
            }
            if (dis[source] + 1 < dis[to])
            {
                dis[to] = dis[source] + 1;
                if (dis[to] < ans)
                {
                    sources[i] = to;
                    lasts[i] = source;
                    i++;
                }
            }
            else
            {
                ans = min(ans, dis[source] + 1 + dis[to]);
            }
        }
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, s;
        cin >> n >> s;
        s--;
        forn(i, n)
        {
            edges[i].clear();
        }
        memset(col, 0, n);
        fill(dis, dis + n, ME);
        ans = ME;
        int order[MAXN];
        forn(i, n - 1)
        {
            cin >> order[i];
            order[i]--;
        }
        forn(i, n - 1)
        {
            int fr, to;
            cin >> fr >> to;
            fr--;
            to--;
            edges[fr].push_back(to);
            edges[to].push_back(fr);
        }
        dis[s] = 0;
        dfs(s);
        col[s] = 1;
        forn(i, n - 1)
        {
            int c = order[i];
            dis[c] = 0;
            dfs(c);
            col[c] = 1;
            if (i)
            {
                cout << ' ';
            }
            cout << ans;
        }
        cout << endl;
    }
}
