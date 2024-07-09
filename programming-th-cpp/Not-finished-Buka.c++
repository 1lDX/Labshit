#include <iostream>
using namespace std;

int main(){
    unsigned long long int a,b,c;
    string o;
    cin>>a>>o>>b;
    if(o=="+"){
        c = a+b;
    }else if (o=="*"){
        c = a*b;
    } 
    cout<<c;
}