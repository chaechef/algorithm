//
// Created by chea1 on 2020-05-16.
//
#include <iostream>
#include <vector>

#define endl "\n"
using namespace std;

int n,k;
int city[51][51];
int mindist = 100000000;
vector<pair<int,int>> houses;
vector<pair<int,int>> chickens;

void Input() {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> city[i][j];
            if (city[i][j] == 1) {
                houses.push_back(make_pair(i,j));
            }else if (city[i][j] == 2) {
                chickens.push_back(make_pair(i,j));
            }
        }
    }
}

int getDistance(vector<pair<int,int>> picked ) {
    int sum = 0;

    for (int i = 0; i < houses.size(); ++i) {
        int temp = 10000000;
        for (int j = 0; j < picked.size(); ++j) {
            temp = min(abs(houses[i].first - picked[j].first) + abs(houses[i].second - picked[j].second),temp);
        }
        sum += temp;
    }
    return sum;
}

void combination(int idx, int count, vector<pair<int,int>> picked) {
    if (count == k) {
        int ret = getDistance(picked);
        mindist = min(ret, mindist);
    }

    for (int i = idx; i < chickens.size(); ++i) {
        picked.push_back(chickens[i]);
        combination(i+1,count+1, picked);
        picked.pop_back();
    }

}

void Solve() {
    vector<pair<int,int>> temp;
    combination(0,0, temp);
    cout << mindist << endl;
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    Solve();

}