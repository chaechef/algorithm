//
// Created by chea1 on 2020-05-13.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int tc, n, k;
    cin >> tc;
    for (int t = 0; t < tc; ++t) {
        vector<int> arr;
        cin >> n >> k;
        if ( (n-k+1 > 0) && (n-k+1) % 2 == 1) {
            for (int i = 0; i < k - 1; ++i) {
                arr.push_back(1);
            }
            arr.push_back(n-k+1);
        }else if ( (n - 2*(k-1) > 0) && (n - 2*(k-1)) % 2 == 0) {
            for (int i = 0; i < k - 1; ++i) {
                arr.push_back(2);
            }
            arr.push_back(n - 2 * (k-1));
        }
        if (arr.size() == 0) {
            cout << "NO" <<endl;
        }else {
            cout << "YES" << endl;
            for (int i = 0; i < arr.size(); ++i) {
                cout << arr[i] << " ";
            }
            cout <<endl;
        }
    }
}