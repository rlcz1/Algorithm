#include <iostream>

using namespace std;

int main(void) {
    int N;
    cin >> N;

    int arr[N];
    
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    int sum = 0;
    for(int i = 0; i < N; i++) {
        sum += arr[i];
        cout << sum << ' ';
    }

    return 0;
}
