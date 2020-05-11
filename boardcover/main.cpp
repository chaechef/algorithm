//
// Created by chea1 on 2020-05-10.
//
#include <iostream>
#include <vector>

using namespace std;

int tc, n, m;
int tile[4][3][2] = {
        {{0,0},{0,1},{1,1}},
        {{0,0},{1,0},{1,1}},
        {{0,0},{0,1},{1,0}},
        {{0,0},{1,0},{1,-1}}
};

bool inRange(int y, int x) {
    if ( y >= 0 && y < n && x >= 0 && x < m) {
        return true;
    }else{
        return false;
    }
}

void printboard(vector<vector<int>>& board){
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << board[i][j] << " ";
        }
        cout<< endl;
    }
}
int recursion(vector<vector<int>>& board, int count) {
//    printboard(board);
    if ( count == 0 ){
        return 1;
    }
    int cx = -1, cy = -1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (board[i][j] == 0) {
                cy = i, cx = j;
                break;
            }
        }
        if (cx != -1) break;
    }
    int res = 0;
    for (int i = 0; i < 4; ++i) {
        bool check = true;
        for (int j = 0; j < 3; ++j) {
            int ny = cy + tile[i][j][0], nx = cx + tile[i][j][1];
            if (board[ny][nx] != 0 || !inRange(ny,nx)) {
                check = false;
            }
        }
        if (check == true) {
            for (int j = 0; j < 3; ++j) {
                int ny = cy + tile[i][j][0], nx = cx + tile[i][j][1];
                board[ny][nx] = 1;
            }
            res += recursion(board, count-1);
            for (int j = 0; j < 3; ++j) {
                int ny = cy + tile[i][j][0], nx = cx + tile[i][j][1];
                board[ny][nx] = 0;
            }
        }
    }
    return res;


}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> tc;
    for (int t = 0; t < tc; ++t) {
        cin >> n >> m;
        vector<vector<int>> arr(n,vector<int>(m,0));
        int count = 0;
        for (int i = 0; i < arr.size(); ++i) {
            for (int j = 0; j < arr[0].size(); ++j) {
                char ch;
                cin >> ch;
                arr[i][j] = ch == '#' ? 1 : 0;
                if (arr[i][j] == 0) {
                    count += 1;
                }
            }
        }
        if ( count % 3 != 0 ) {
            cout << 0 << endl;
        }else {
            int res = recursion(arr, count/3);
            cout << res << endl;
        }

    }

}
