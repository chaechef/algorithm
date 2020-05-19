//
// Created by chea1 on 2020-05-11.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    vector<int> nanjang(9,0);

    for (int i = 0; i < 9; ++i) {
        scanf("%d", &nanjang[i]);
    }
    sort(nanjang.begin(),nanjang.end());

    for (int i = 0; i < 9; ++i) {
        int sum = 0;
        for (int j = i; j < 9; ++j) {
            sum = 0;
            for (int k = 0; k < 9; ++k) {
                if (k != i && k != j) {
                    sum += nanjang[k];
                }
            }
            if (sum == 100) {
                for (int k = 0; k < 9; ++k) {
                    if (k != i && k != j) {
                        cout << nanjang[k] << " ";
                    }
                }
                cout << endl;
                return 0;
            }
        }
    }

}