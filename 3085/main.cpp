#include <iostream>
#include <vector>

using namespace std;

int n;
vector<string> bom;
int dy[2]{1,0};
int dx[2]{0,1};

bool inRange(int y, int x) {
    if (y >= n || x >= n){
        return false;
    }else {
        return true;
    }
}

void swap(char& a, char& b){
    char temp;
    temp = a;
    a = b;
    b = temp;
}


int checkMaxCandy() {
    int totalmaxcount = 1;

    for (int i = 0; i < n; ++i) {
        char prevcandy = bom[i][0];
        int currcount = 1;
        int maxcount = 1;
        for (int j = 1; j < n; ++j) {
            if (prevcandy == bom[i][j]) {
                currcount++;
            }else{
                prevcandy = bom[i][j];
                maxcount = max(maxcount, currcount);
                currcount = 1;
            }
        }
        maxcount = max(maxcount,currcount);
        totalmaxcount = max(totalmaxcount, maxcount);
    }

    for (int i = 0; i < n; ++i) {
        char prevcandy = bom[0][i];
        int currcount = 1;
        int maxcount = 1;
        for (int j = 1; j < n; ++j) {
            if (prevcandy == bom[j][i]) {
                currcount++;
            }else{
                prevcandy = bom[j][i];
                maxcount = max(maxcount, currcount);
                currcount = 1;
            }
        }
        maxcount = max(maxcount,currcount);
        totalmaxcount = max(totalmaxcount, maxcount);
    }

    return totalmaxcount;
}
int main() {
    cin >> n;
    int totalcount = 1;
    for (int i = 0; i < n; ++i) {
        string temp;
        cin >> temp;
        bom.push_back(temp);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < 2; ++k) {
                int ny = i + dy[k], nx = j + dx[k];
                if (inRange(ny,nx) && bom[i][j] != bom[ny][nx]) {
                    swap(bom[i][j], bom[ny][nx]);
                    int res = checkMaxCandy();
                    totalcount = max(totalcount,res);
                    swap(bom[i][j], bom[ny][nx]);
                }
            }
        }
    }
    cout << totalcount << endl;
}