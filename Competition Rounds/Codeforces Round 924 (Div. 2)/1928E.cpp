#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

const int MAXN = 2e5 + 5;

ll dp_v[MAXN];
ll dp_h[MAXN];

void precompute() {
  dp_v[0] = 0;
  dp_h[0] = 0;

  for (int i = 1; i < MAXN; i++) {
    ll shortest = 3 * i;
    ll prev = 0;
    for (int j = 1; j < 460; j++) {
      ll cnt = (j * (j + 1)) / 2;
      if (cnt > i) {
        break;
      }
      if (j + 1 > shortest) {
        break;
      }
      ll rem = dp_v[i - cnt];
      if (rem + j + 1 < shortest) {
        shortest = rem + j + 1;
        prev = j;
      }
    }
    dp_v[i] = shortest;
    dp_h[i] = prev;
  }
}

int main() {
  precompute();
  int t;
  cin >> t;
  ll ans[MAXN];
  while (t--) {
    ll n, x, y, s;
    cin >> n >> x >> y >> s;
    ll r = x % y;
    ll minv = r * (n - 1) + x;
    ll dif = s - minv;
    if (dif < 0 || dif % y != 0) {
      cout << "NO" << endl;
      continue;
    }
    bool found = false;
    ll total = (s - r * n) / y;
    for (int i = 0; i < n; i++) {
      ans[i] = 0;
    }
    ans[0] = (x - r) / y;
    for (int i = 0; i < n; i++) {
      ans[i] = ans[0] + i;
      total -= ans[i];
      if (total < 0) {
        break;
      }
      if (total == 0) {
        found = true;
        break;
      }
      if (i == n - 1) {
        break;
      }
      ll rem = n - i - 1;
      if (dp_v[total] > rem) {
        continue;
      }
      // cout << "found at" << i << endl;
      // cout << "total " << total << endl;
      // cout << "dp_v " << dp_v[total] << dp_h[total] << endl;
      ll ar = dp_h[total];
      ll ind = i + 1;
      while (ar) {
        for (int j = 0; j <= ar; j++) {
          ans[ind++] = j;
        }
        total -= ar * (ar + 1) / 2;
        ar = dp_h[total];
      }
      found = true;
      break;
    }
    if (found) {
      cout << "YES" << endl;
      for (int i = 0; i < n; i++) {
        cout << r + ans[i] * y << " ";
      }
      cout << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}