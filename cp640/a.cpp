//
// Created by chea1 on 2020-05-13.
//
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; ++i) {
        int number;
        int unit = 1;
        vector<int> ans;
        cin >> number;

        while (number > 0) {
            int curr = number % 10;
            if (curr != 0) {
                ans.push_back(unit*curr);
            }
            unit *= 10;
            number /= 10;
        }

        cout << ans.size() <<endl;
        for (int j = 0; j < ans.size(); ++j) {
            cout << ans[j] << " ";
        }
        cout << endl;
    }
}