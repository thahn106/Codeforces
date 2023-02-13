#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)
using namespace std;

int main()
{
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};

    int t;
    cin >> t;
    while (t--)
    {
        int N, M;
        cin >> N >> M;
        auto bc = [&](int y, int x)
        { return 0 <= y && y < N && 0 <= x && x < M; };

        vector<string> matrix(N);
        vector<vector<int>> empty_neighbors(N, vector<int>(M, 0));
        vector<vector<bool>> visited(N, vector<bool>(M, 0));
        queue<pair<int, int>> remaining;

        forn(n, N)
        {
            cin >> matrix[n];
            forn(m, M)
            {
                if (matrix[n][m] == 'L')
                {
                    remaining.push(make_pair(n, m));
                    visited[n][m] = true;
                }
            }
        }
        int p = 0;
        forn(n, N) forn(m, M) if (matrix[n][m] == '.')
        {
            forn(i, 4)
            {
                int ny = n + dy[i];
                int nx = m + dx[i];
                empty_neighbors[n][m] += (bc(ny, nx) && matrix[ny][nx] != '#');
            }
        }
        while (!remaining.empty())
        {
            int n = remaining.front().first;
            int m = remaining.front().second;
            remaining.pop();
            forn(i, 4)
            {
                int ny = n + dy[i];
                int nx = m + dx[i];
                if (!bc(ny, nx) || matrix[ny][nx] == '#' || visited[ny][nx])
                {
                    continue;
                }
                if (--empty_neighbors[ny][nx] <= 1)
                {
                    visited[ny][nx] = true;
                    matrix[ny][nx] = '+';
                    remaining.push(make_pair(ny, nx));
                }
            }
        }
        forn(n, N) printf("%s\n", matrix[n].c_str());
    }
}