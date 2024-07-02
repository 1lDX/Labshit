#include <bits/stdc++.h>
using namespace std;

int main() {

    // 1. init iterator variable
    // 2. conidtion
    // 3. increase iterator variable

    // string str[50]; // index: 0, 1, 2, 3, 4
    // str[0] = "Hello";
    // str[1] = "World";
    // str[2] = "Nong ja";
    // str[3] = "Nong Heng";
    // str[4] = "Comsci";

    // for (int i=0; i<50; i++) {
    //     cout << str[i] << '\n';
    // }


    
    int k,j;
    cout << "Input value of k: ";
    cin >> k;
    string str[k];
    for (j=0; j<k; j++) {
        cout << "Input str index " << j << " : ";
        cin >> str[j];
    }

    for (int j=0; j<k; j++) {
        cout << "str index " << j << ' '<< str[j] << '\n';
    }

    return 0;
}