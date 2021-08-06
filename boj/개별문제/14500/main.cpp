//
// Created by chea1 on 2020-05-15.
//
#include <iostream>
#include <vector>

using namespace std;

int dy[4]{1,-1,0,0};
int dx[4]{0,0,1,-1};
int n, m;
vector<vector<int>> board;
vector<vector<bool>> visited;

bool inRange(int y, int x) {
    if (y >= 0 && y < n && x >= 0 && x < m) {
        return true;
    }else{
        return false;
    }
}

int dfs(int y, int x, int sum, int count) {
    if (count == 4) {
        return sum;
    }
    visited[y][x] = 1;
    int tempmax = 0;

    for (int i = 0; i < 4; ++i) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (inRange(ny,nx) && !visited[ny][nx]) {
            int ret = dfs(ny,nx,sum+board[y][x], count + 1);
            tempmax = max(tempmax,ret);
        }
    }
    visited[y][x] = 0;
    return tempmax;

}


int main() {
    cin >> n >> m;
    board.resize(n);
    visited.resize(n);
    for (int i = 0; i < n; ++i) {
        board[i].resize(m);
        visited[i].resize(m);
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> board[i][j];
        }
    }
    int maxsum = 0;
//    cout << dfs(0,0,0,0) << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int ret = dfs(i,j,0,0);
            maxsum = max(maxsum,ret);
            if (inRange(i-1,j+1) && inRange(i,j+1) && inRange(i+1,j+1)){
                int temp = board[i][j] + board[i-1][j+1] + board[i][j+1] + board[i+1][j+1];
                maxsum = max(maxsum, temp);
            }
            if (inRange(i+1,j+1) && inRange(i+1,j) && inRange(i+1,j-1)){
                int temp = board[i][j] + board[i+1][j+1] + board[i+1][j] + board[i+1][j-1];
                maxsum = max(maxsum, temp);
            }
            if (inRange(i-1,j-1) && inRange(i,j-1) && inRange(i+1,j-1)){
                int temp = board[i][j] + board[i-1][j-1] + board[i][j-1] + board[i+1][j-1];
                maxsum = max(maxsum, temp);
            }
            if (inRange(i-1,j+1) && inRange(i-1,j) && inRange(i-1,j-1)){
                int temp = board[i][j] + board[i-1][j+1] + board[i-1][j] + board[i-1][j-1];
                maxsum = max(maxsum, temp);
            }


        }
    }
    cout << maxsum << endl;
}


