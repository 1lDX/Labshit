#include <iostream>
using namespace std;

int main(){
    int n,i,j,k,x;

    cin>>n;

    if (n == 1){
        cout << "#";
    }
    else {

        // Make Full roll
        for(j = 0; j < n; j++){
            cout << "#";
        }
        cout << "\n";
        // Make Space roll
        for(k = 0; k < n - 2; k++){
            cout << "#";
            for (j = 0; j < n - 2; j++)
            {
                cout << " ";
            }
            cout << "#";
            cout << "\n";
        }
        for(j = 0; j < n; j++){
            cout << "#";
        }
    }
}
