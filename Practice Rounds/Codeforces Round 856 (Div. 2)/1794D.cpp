#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

const ll MOD = 998244353;
const int MAXP = 1 << 20;
const int MAXN = 4050;

bool is_prime[MAXP];
ll fac[MAXN];
ll faci[MAXN];
ll dp[MAXN][MAXN];
vector<int> pp, cp;

const string sp = " ";

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
    memset(is_prime, true, sizeof(is_prime));
    is_prime[0] = false;
    is_prime[1] = false;

    for (int i = 2; i < MAXP; i++)
    {
        if (is_prime[i])
        {
            int ind = 2 * i;
            while (ind < MAXP)
            {
                is_prime[ind] = false;
                ind += i;
            }
        }
    }
    fac[0] = 1;
    faci[0] = 1;
    for (int i = 1; i < MAXN; i++)
    {
        fac[i] = ((fac[i - 1] * i) % MOD);
        faci[i] = fp(fac[i], MOD - 2);
    }
}

ll dpc(ll x, ll y)
{
    ll &res = dp[x][y];
    if (res >= 0)
    {
        return res;
    }
    if (x == pp.size())
    {

        res = (y == 0);
        return res;
    }
    res = (faci[pp[x]] * dpc(x + 1, y)) % MOD;
    if (y > 0)
    {
        res = (res + faci[pp[x] - 1] * dpc(x + 1, y - 1)) % MOD;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    precompute();
    int N;
    cin >> N;
    vector<int> a(2 * N);
    forn(i, 2 * N)
    {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int last = a[0];
    int cur = 0;

    for (auto x : a)
    {
        if (x == last)
        {
            cur++;
        }
        else
        {
            if (is_prime[last])
            {
                pp.push_back(cur);
            }
            else
            {
                cp.push_back(cur);
            }
            last = x;
            cur = 1;
        }
    }
    if (is_prime[last])
    {
        pp.push_back(cur);
    }
    else
    {
        cp.push_back(cur);
    }
    if (pp.size() < N)
    {
        cout << 0 << "\n";
        return 0;
    }
    memset(dp, -1, sizeof(dp));

    ll ans = fac[N];
    ans = (dpc(0, N) * ans) % MOD;
    for (auto x : cp)
    {
        ans = (ans * faci[x]) % MOD;
    }
    cout << ans << "\n";
}
