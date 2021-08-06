#include <iostream>

using namespace std;

int main(){
    while (true) {
        int t1, t2;
        cin >> t1 >> t2;
        if (t1 == 0 && t2 == 0){
            break;
        }else {
            cout << t1 + t2 << endl;
        }

    }
}