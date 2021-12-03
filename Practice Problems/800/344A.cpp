#include<iostream>
using namespace std;

int main(){
  int N;
  cin >>N;
  int count=0;
  int prev=0;
  int temp;
  for (int i =0;i<N;i++){
    cin >> temp;
    if (prev!=temp){
      count++;
      prev = temp;
    }
  }
  cout << count << endl;
}
