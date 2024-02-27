#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int main() {
  // ios::sync_with_stdio(false);
  // cin.tie(0);
  int t;
  cin >> t;
  vector<int> c;
  vector<vector<int>> graph;
  vector<ull> exposed;
  stack<pii> s;
  stack<ull> col_stacks;
  vector<bool> visited;
  while (t--) {
    int n;
    cin >> n;

    c.clear();
    c.resize(n + 1, 0);
    graph.clear();
    graph.resize(n + 1, vector<int>());
    exposed.clear();
    exposed.resize(n + 1, 0);
    visited.clear();
    visited.resize(n + 1, false);
    while (!s.empty()) s.pop();
    while (!col_stacks.empty()) col_stacks.pop();

    for (int i = 1; i <= n; i++) {
      cin >> c[i];
    }

    for (int i = 1; i <= n - 1; i++) {
      int u, v;
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    // dummy node to make it easier
    graph[0].push_back(1);
    graph[1].push_back(0);

    s.push({0, 0});
    s.push({1, 0});
    ull ans = 0;

    while (!s.empty()) {
      auto [node, ind] = s.top();
      s.pop();
      if (node == 0) break;
      // cout << "node: " << node << " ind: " << ind << endl;
      // cout << "stacksize: " << s.size()
      //      << " col_stacksize: " << col_stacks.size() << endl;

      int col = c[node];
      int child_count = graph[node].size();
      if (ind == 0) {
        ans += exposed[col];
        col_stacks.push(exposed[col]);
        exposed[col] = 1;
      }

      if (ind < child_count) {
        int next = graph[node][ind];
        int top = s.top().first;
        s.push({node, ind + 1});
        if (next == top) {
          continue;
        }
        exposed[col] = 1;
        s.push({next, 0});
      }
      if (ind >= child_count) {
        exposed[col] = col_stacks.top();
        col_stacks.pop();
        exposed[col]++;
      }
    }
    cout << ans << '\n';
  }
}