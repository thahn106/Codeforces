#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;
typedef long long ll;

int solve()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    forn(i, n)
    {
        cin >> arr[i];
    }
    int last = 1 << 30;
    forn(i, n)
    {
        while (arr[i] == 1 || arr[i] % last == 0)
        {
            arr[i]++;
        }
        last = arr[i];
        if (i)
        {
            cout << " ";
        }
        cout << last;
    }
    cout << "\n";
    return 0;
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
