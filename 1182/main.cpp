//
// Created by chea1 on 2020-05-15.
//
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int count = 0;
int n, m;
vector<int> arr;


void recursion(vector<int> picked, int idx) {
    if (idx == n ) {
        int sum = accumulate(picked.begin(),picked.end(),0);
        if (sum == m && picked.size() > 0) {
            count ++;
        }
        return;
    }

    recursion(picked, idx+1);
    picked.push_back(arr[idx]);
    recursion(picked, idx+1);

}

int main() {
    cin >> n >> m;
    arr.resize(n);
    vector<int> temp;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    recursion(temp, 0);
    cout << count << endl;

}