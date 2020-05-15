//
// Created by chea1 on 2020-05-15.
//
#include <iostream>
#include <vector>

using namespace std;

int check(vector<string> &board, int y, int x, int type) {
    int count = 0;
    for (int i = y; i < y+8; ++i) {
        for (int j = x; j < x+8; ++j) {
            if ((i+j) % 2 == type) {
                if (board[i][j] == 'W') {
                    count++;
                }
            }else{
                if (board[i][j] == 'B') {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int n, m; cin >> n >> m;
    vector<string> board;
    for (int i = 0; i < n; ++i) {
        string temp;
        cin >> temp;
        board.push_back(temp);
    }

    int ret = 64;
    for (int i = 0; i <= n - 8; ++i) {
        for (int j = 0; j <= m - 8; ++j) {
            int minchange = min(check(board, i, j, 0), check(board, i, j, 1));
            ret = min(ret, minchange);
        }
    }
    cout << ret << endl;
}
