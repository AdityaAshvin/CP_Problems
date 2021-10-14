#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
int main()
{
    
    char a[55][55];
    int n,m;
    
    while(cin>>n>>m){
        int mini=inf,minj=inf,maxi=0,maxj=0;
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
                if(a[i][j]=='*'){
                    mini=min(mini,i);
                    minj=min(minj,j);
                    maxi=max(maxi,i);
                    maxj=max(maxj,j);
                }
            }
        }
        for(i=mini;i<=maxi;i++){
            for(j=minj;j<=maxj;j++){
                cout<<a[i][j];
            }
            cout<<endl;
        }
    }


    return 0;
}
