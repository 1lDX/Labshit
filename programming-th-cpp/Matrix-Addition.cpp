#include <iostream>
using namespace std;

int main(){
    int i,j,x,z,g,c,y,v;
    cin>>i>>j;
    int arr[i][j];
    int plus[i][j];
    int sum[i][j];

    //matrix nxn
    for(x=0;x<i;x++){
        for(y=0;y<j;y++){
            cin>>arr[x][y];
        }
    }
    //matrix add
    for(z=0;z<i;z++){
        for(v=0;v<j;v++){
            cin>>plus[z][v];
        }
    }
    //matrix process
    for(c=0;c<i;c++){
        for(g=0;g<j;g++){
            sum[c][g] = plus[c][g]+arr[c][g];
            cout<<sum[c][g]<<" ";
        }
        cout<<"\n";
    }  
}