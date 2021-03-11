//
// Created by chea1 on 2020-05-10.
//
#include <iostream>
#include <vector>
using namespace std;

void pick(int n, vector<int> &picked, int topick) {

    if(topick == 0) {
        for (int i = 0; i < picked.size(); ++i) {
            cout << picked[i] << " ";
        }
        cout << endl;
        return;
    }

    int smallest = picked.empty() ? 0 : picked.back() + 1;

    for (int j = smallest; j < n; ++j) {
        picked.push_back(j);
        pick(n, picked, topick-1);
        picked.pop_back();
    }
}

int main() {
    vector<int> a;
    pick(5, a, 3);
}

