#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

void solve()
{
    int n;
    cin >> n;
    int last = 0;
    vector<int> arr(n);
    forn(i, n)
    {
        int cur;
        cin >> arr[i];
        if (arr[i - last] >= last + 1)
        {
            last++;
        }
        if (i)
        {
            cout << " ";
        }
        cout << last;
    }
    cout << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
