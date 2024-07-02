#include <iostream>
#include <string>
using namespace std;

int main(){
    //make variable
    int i,j,k,z,x,u;
    //input
	cout<<"Enter Row space : ";
    cin>>j;
	cout<<"Enter Column space : ";
	cin>>k;
    //make array
    int array[j][k];
      for(z=0;z<j;z++){
        for(x=0;x<k;x++){
			cin>>array[z][x];
        }

    }
    //input check number
    cin>>u;
    
    for(z=0;z<j;z++){
        for(x=0;x<k;x++){
            //check if array = check number
            if(array[z][x] != u){
                cout<<"*"<<" ";
            }else{
                cout<<u<<" ";
            }
            }

             if(array[z][x] == array[z][k]){
                cout<<"\n";
            }

            
    }
    return 0;

}
