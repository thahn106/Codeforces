#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    vector<long long> a;
    vector<pair<long long, bool>> base;
    set<long long> difset;
    while (t--)
    {
        long long n, k;
        cin >> n >> k;
        a.clear();
        a.resize(n);
        for (long long i = 0; i < n; i++)
            cin >> a[i];
        long long ans;
        if (k >= 3)
        {
            ans = 0;
        }
        else if (k == 1)
        {
            sort(a.begin(), a.end());
            ans = a[0];
            for (long long i = 1; i < n; i++)
                ans = min(ans, a[i] - a[i - 1]);
        }
        else if (k == 2)
        {
            sort(a.begin(), a.end());
            ans = a[0];
            difset.clear();
            base.clear();
            for (long long i = 1; i < n; i++)
                for (long long j = 0; j < i; j++)
                    difset.insert(abs(a[i] - a[j]));
            for (auto x : difset)
                base.push_back({x, false});
            for (auto x : a)
                base.push_back({x, true});
            sort(base.begin(), base.end());
            for (long long i = 0; i < base.size(); i++)
            {
                if (base[i].second)
                {
                    if (i > 0)
                        ans = min(ans, base[i].first - base[i - 1].first);
                    if (i < base.size() - 1)
                        ans = min(ans, base[i + 1].first - base[i].first);
                }
            }
        }

        cout << ans << endl;
    }
}
