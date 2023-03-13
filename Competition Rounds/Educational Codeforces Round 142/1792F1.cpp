#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

const string EL = "\n";

const int MAXN = 50050;
const int MOD = 998244353;

ll fac[MAXN];
ll faci[MAXN];
ll dpa[MAXN];
ll dpb[MAXN];

ll fp(ll b, ll e)
{
    ll res = 1;
    while (e > 0)
    {
        if (e % 2)
        {
            res = res * b % MOD;
        }
        b = b * b % MOD;
        e /= 2;
    }
    return res;
}

void precompute()
{
    fac[0] = 1;
    faci[0] = 1;
    for (int i = 1; i < MAXN; i++)
    {
        fac[i] = ((fac[i - 1] * i) % MOD);
        faci[i] = fp(fac[i], MOD - 2);
    }
}
ll mul(ll a, ll b)
{
    return (a * b) % MOD;
}

int solve()
{
    precompute();
    int N;
    cin >> N;
    dpa[1] = 1;
    dpb[1] = 1;
    for (int i = 2; i <= N; i++)
    {
        dpb[i] = 0;
        for (int j = 1; j < i; j++)
        {
            ll t = 1;
            t = mul(t, dpb[j]);
            t = mul(t, dpa[i - j]);
            t = mul(t, fac[i - 1]);
            t = mul(t, faci[j - 1]);
            t = mul(t, faci[i - j]);
            dpb[i] = (dpb[i] + t) % MOD;
        }
        dpa[i] = 2 * dpb[i];
    }
    cout << (dpa[N] - 2) % MOD << EL;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
