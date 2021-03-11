//
// Created by chea1 on 2020-05-12.
//
#include <iostream>
#include <vector>

using namespace std;


int tc, n;
vector<int> fences;


int dq(int start, int end) {
    int mid = (start + end) / 2;
    if (start == end ){
        return fences[start];
    }
    int t1 = dq(start, mid);
    int t2 = dq(mid+1, end);

    int minheight = fences[mid];
    int lo = mid -1;
    int hi = mid +1;

    while (lo >= start && hi <= end) {

    }

}


int main() {
    cin >> tc;
    for (int i = 0; i < tc; ++i) {
        cin >> n;
        fences.resize(n);
        for (int j = 0; j < n; ++j) {
            cin >> fences[j];
        }

        int ret = dq(0,n);



    }
}