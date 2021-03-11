//
// Created by chea1 on 2020-06-04.
//

#include <iostream>

using namespace std;

int main() {
    while (true) {
        int t1, t2;
        cin >> t1 >> t2;
        if (cin.eof()) {
            break;
        }
        cout << t1 + t2 << endl;
    }
}