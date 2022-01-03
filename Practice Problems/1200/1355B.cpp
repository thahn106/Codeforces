#include<bits/stdc++.h>
using namespace std;

const int MAXN = 200005;

int main(){
  int T;
  cin >> T;
  for (int t =0; t<T; t++){
    int explorers[MAXN];
    int N;
    cin >> N;
    for (int n=0;n<N;n++){
      cin >> explorers[n];
    }
    int ans = 0;
    int run = 0;
    sort(explorers, explorers+N);
    for (int n=0;n<N;n++){
      run++;
      if (explorers[n] < run+1){
        ans++;
        run = 0;
      }
    }
    cout << ans << endl;
  }
}
