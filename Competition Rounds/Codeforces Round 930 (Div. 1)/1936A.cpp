#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

int query(int a, int b, int c, int d) {
  cout << "? " << a << " " << b << " " << c << " " << d << endl;
  char x;
  cin >> x;
  if (x == '<') {
    return -1;
  } else if (x == '>') {
    return 1;
  }
  return 0;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int li = 0;
    for (int i = 1; i < n; i++) {
      int q = query(li, li, i, i);
      if (q == -1) {
        li = i;
      }
    }
    vector<int> ans;
    ans.clear();
    int best = li;
    // cout << "finding cands" << endl;
    for (int i = 0; i < n; i++) {
      if (i == li) {
        continue;
      }
      int q = query(li, best, li, i);
      if (q == -1) {
        ans.clear();
        ans.push_back(i);
        best = i;
      } else if (q == 0) {
        ans.push_back(i);
      }
    }
    // cout << "finding small" << endl;
    int small = ans[0];
    for (int i = 1; i < ans.size(); i++) {
      int q = query(ans[i], ans[i], small, small);
      if (q == -1) {
        small = ans[i];
      }
    }
    cout << "! " << small << " " << li << endl;
  }

  return 0;
}