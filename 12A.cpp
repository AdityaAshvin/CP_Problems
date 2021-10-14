#include <bits/stdc++.h>
using namespace std; 
int main()
{
    string a,b,c;
    cin>>a;
    cin>>b;
    cin>>c;
    a.append(b);
    a.append(c);
    bool t=true;
    int n=a.length();
    for(int i=0;i<(n/2);i++){
        if(a[i]!=a[n-i-1]){
            t=false;
        }
    }
    
    if(t)
        cout<<"YES";
    else
        cout<<"NO";
        
    return 0;
}
