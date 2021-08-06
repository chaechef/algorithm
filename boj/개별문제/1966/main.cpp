//
// Created by chea1 on 2020-05-14.
//

#include <iostream>
#include <queue>


using namespace std;

bool check(int idx, int arr[]) {
    bool ok = true;
    for (int i = idx+1; i < 10 ; ++i) {
        if (arr[i] != 0) {
            return false;
        }
    }
    return ok;
}

int main() {
    int tc; cin >> tc;
    while (tc--) {
        int n ,k;
        cin >> n >> k;
        queue<pair<int,int>> printqueue;
        int priority[10]{0};

        for (int i = 0; i < n; ++i) {
            int temp; cin >>temp;
            priority[temp]++;
            printqueue.push(make_pair(i,temp));
        }
        int count = 1;
        while (true) {
            pair<int,int> curr = printqueue.front();
            if (curr.first == k && check(curr.second, priority)){
                cout << count << endl;
                break;
            }else if(check(curr.second, priority)){
                priority[curr.second]--;
                printqueue.pop();
                count++;
            }else {
                printqueue.pop();
                printqueue.push(curr);
            }
        }
    }
}