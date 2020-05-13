//
// Created by chea1 on 2020-05-13.
//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int number;

bool pick(vector<int>& nums, vector<int>& picked ,int topick, int idx) {
    if (topick == 0) {
            if (number == (picked[0] + picked[1] + picked[2])) {
                return true;
            }else {
                return false;
            }
    }
    bool check = false;
    for (int i = idx; i < nums.size(); ++i) {
        picked.push_back(nums[i]);
        check = pick(nums, picked, topick-1, i);
        if (check) {
            return check;
        }
        picked.pop_back();
    }
    return check;
}

int main() {
    int tc; cin >> tc;

    for (int i = 0; i < tc; ++i) {
        cin >> number;
        vector<int> trianglenumber ,picked;
        int prev = 1;
        int differ = 2;
        while (prev < 1001) {
            trianglenumber.push_back(prev);
            prev += differ;
            differ++;
        }
        if (trianglenumber.size() < 3) {
            cout << 0 << endl;
            continue;
        }

        if (pick(trianglenumber, picked, 3, 0)){
            cout << 1 << endl;
        }else {
            cout << 0 << endl;
        }



    }


}