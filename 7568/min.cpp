//
// Created by chea1 on 2020-05-14.
//

#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> v;
int n;
int main() {
    cin >> n;
    v.resize(n);

    for (int i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }
    for (int i = 0; i < n; ++i) {
        int count = 0;
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                if (v[i].first < v[j].first && v[i].second < v[j].second) {
                    count++;
                }
            }
        }
        cout << count + 1 << " ";
    }
    cout << endl;


}