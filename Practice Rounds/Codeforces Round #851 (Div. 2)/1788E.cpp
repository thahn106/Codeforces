#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

int n;
ll a[200005];
const ll INF = 1LL << 61;

void input()
{
    cin >> n;
    forn(i, n)
    {
        cin >> a[i];
    }
}
void solve()
{
    ll pre[200005];
    ll cur = 0;
    forn(i, n)
    {
        cur += a[i];
        pre[i + 1] = cur;
    }
    set<pair<ll, ll>> S;
    S.insert({0, 0});
    ll dp[200005];
    dp[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        dp[i] = dp[i - 1] + 1;
        auto it = S.lower_bound({pre[i], INF});
        if (it != S.begin())
        {
            dp[i] = min(dp[i], prev(it)->second);
        }
        pair<ll, ll> p = {pre[i], dp[i]};
        it = S.lower_bound(p);
        if (it != S.begin() && prev(it)->second <= dp[i])
        {
            continue;
        }
        S.insert(p);
        it = S.find(p);
        it++;
        while (it != S.end())
        {
            if (it->second >= dp[i])
            {
                it = S.erase(it);
            }
            else
            {
                break;
            }
        }
    }
    cout << n - dp[n] << endl;
}

int main()
{
    input();
    solve();
}
