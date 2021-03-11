//
// Created by chea1 on 2020-05-12.
//

#include <iostream>
#include <vector>

using namespace std;

int tc;
string input;

string reverse(string::iterator& it) {
    char head = *it;
    ++it;
    if (head == 'b' || head == 'w')
        return string(1, head);
    string ul = reverse(it);
    string ur = reverse(it);
    string ll = reverse(it);
    string lr = reverse(it);
    return string("x") + ll + lr + ul + ur;

}

int main() {
    cin >> tc;
    for (int i = 0; i < tc; ++i) {
        cin >> input;
        string::iterator it = input.begin();
        string res = reverse(it);
        cout << res <<endl;
    }
}