#include <iostream>
#include<string>
#include<vector>

using namespace std;

int main(void) {
    string S;
    getline(cin, S);
    vector <char> sv;
    
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == '(') {
            sv.push_back(S[i]);
        }
    }
    
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == ')') {
            sv.pop_back();
        }
    }
    
    if (sv.empty() == 1) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}
