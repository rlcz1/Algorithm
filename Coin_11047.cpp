#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int N;
    int K;
    cin >> N >> K;

    vector<int> v;

    for (int i = 0; i < N; i++) {
        int k;
        cin >> k;
        v.push_back(k);
    }

    int total = 0;

    while (true) {
        for (int i = N-1; i >= 0; i--) {
            if (v[i] <= K) {
                int cnt = floor(K / v[i]);
                total += cnt;
                K -= cnt * v[i];
                break;
            }
        }

        if (K == 0) {
            break;
        }
    }

    cout << total << endl;

    return 0;
}
