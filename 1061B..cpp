#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  vector<int> s(a);
  long long sum = 0;
  int amx = 1;
  for (int i = 0; i < a; i++) {
    cin >> s[i];
    sum += s[i];
    amx = max(mx, s[i]);
  }
  sort(s.begin(), s.end());
  int ans = sum - max(mx, a);
  if (amx >= a and a > 1 and s[1] == 1) {
    ans--;
  }
  cout << ans << endl;
  return 0;
}
