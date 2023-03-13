#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;
int N, Q;
const int MAXN = 300010;
const ll INF = 1 << 30;
ll a[MAXN];
ll queries[MAXN];

ll ans[MAXN];
ll dp[MAXN];

int input()
{
    cin >> N;
    forn(i, N)
    {
        cin >> a[i];
    }

    cin >> Q;
    forn(i, Q)
    {
        cin >> queries[i];
    }
}

int solve()
{
    sort(a, a + N);
    dp[0] = 0;
    for (ll i = 1; i <= N; i++)
    {
        if (a[i - 1] <= i)
        {
            dp[i] = dp[i - a[i - 1]] + 1;
            ans[dp[i] + N - i] = max(ans[dp[i] + N - i], i);
        }
        else
        {
            if (a[i - 1] <= N)
            {
                ans[N + 1 - a[i - 1]] = max(ans[N + 1 - a[i - 1]], i);
            }
        }
        dp[i] = max(dp[i], dp[i - 1]);
    }
    for (int i = N - 1; i >= 0; i--)
    {
        ans[i] = max(ans[i], ans[i + 1]);
    }

    forn(i, Q)
    {
        cout << ans[queries[i]] << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    input();
    solve();
}
