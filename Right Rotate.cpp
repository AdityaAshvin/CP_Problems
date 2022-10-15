#include<vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> a={1,2,3,4};
    int n=4;
    int t = a[n-1];

    for(int i=n-1;i>0;i--){
        a[i] = a[i-1];
    }
    a[0] = t;

    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
}
