#include <bits/stdc++.h>
using namespace std;
 void solve()

 {
    long long n;
    cin>>n;
    vector<vector<long long>> adj(n+1);
    vector<long long> deg(n+1,0);
    for(long long i=0;i<n-1;i++)
    {
        long long u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
    if (n==1)
    {
        cout<<1<<endl;
        return;
    }
    vector<long long> val(n + 1) ;
    for (long long i = 1; i <= n,i++)
    {
        cin>>val[i];
    }

 }