#include <iostream>

using namespace std;

int main(void) 
{
    string str;
    int N;
    cin >> str >> N;
    int p = 0;
    for (int i = 0; i < N; i++) 
    {
        string a;
        cin >> a;
        if (a.compare("prev") == 0) {
            if (p > 0) p -= 1;
        } 
        else if (a.compare("next") == 0) {
            if (p+2 < str.length()) p += 1;
        } 
        else if (a.compare("left") == 0) {
            if (p > 0) {
                string temp ="";
                for (int j = 0; j < str.length(); j++) {
                    if (p != j) temp += str[j]; 
                }
                p -= 1;
                str = temp;
            }
        } 
        else if (a.compare("right") == 0) {
            if (p+2 < str.length()) {
                string temp ="";
                for (int j = 0; j < str.length(); j++) {
                    if (p+1 != j) temp += str[j]; 
                }
                str = temp;
            }
            
        }
    }
    cout << str[p] << ' ' << str[p+1];
    
    return 0;
}
