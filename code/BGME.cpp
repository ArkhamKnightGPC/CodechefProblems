#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e5 + 7;
int A[MAXN];
set< pair<int,int> > odd, even;

int main() {
	int tc; cin>>tc;
	
	while(tc--){
	    int n; cin>>n;
	    for(int i=0; i<n; i++){
	        cin>>A[i]; //A[i]<=10^9 but we only care about parity!
	        if(A[i]%2 == 0){
	            A[i] = 2;
	            even.insert( make_pair(A[i], i) ); //we add bucket number to work with multiset
	        }else{
	            A[i] = min(A[i], 3);
	            odd.insert( make_pair(A[i], i) );
	        }
	    }
	    int alice = 0;
	    int bob = 0;
	    int turn = 0;
	    while(!even.empty() || !odd.empty()){
	        if(odd.empty()){//only reason to ever play on an even bucket
	            pair<int,int> bi = *(--even.end());
	            even.erase(bi);
	            bi.first--;
	            odd.insert(bi);
	        }else{
	            pair<int,int> bi = *odd.begin();
	            odd.erase(bi);
	            bi.first--;
	            if(bi.first == 0){//someone just got a point!
	                if(turn%2 == 0){//Alice 
	                    alice++;
	                }else{//Bob
	                    bob++;
	                }
	            }else{//bucket is not over yet
	                even.insert(bi);
	            }
	        }
	        turn++;
	    }
	    if(alice > bob){
	        cout<<"ALICE"<<endl;
	    }else if (alice < bob){
	        cout<<"BOB"<<endl;
	    }else{
	        cout<<"DRAW"<<endl;
	    }
	}

}
