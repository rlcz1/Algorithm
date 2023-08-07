#include <iostream>

using namespace std;

int main(void) {
    int N;
    cin >> N;
    
    int *lst;

	lst = (int*)malloc(1 * sizeof(int));
    int cnt = 0;
    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        switch(a) {
            case 1: {
                int b;
                cin >> b;
                cnt++;
                lst = (int *)realloc(lst,sizeof(int) * cnt);
                lst[cnt-1] = b;

                break;
            }
            case 2: {
                if (cnt < 1) {
                    cout << -1 << endl;
                    break;
                }
                int p = lst[cnt-1];
                
                int *temp = (int*)malloc(cnt-- * sizeof(int));
                for(int i = 0; i < cnt; i++) {
                    temp[i] = lst[i];
                }
                lst = temp;

                cout << p << endl;
                break;
            }
            case 3: {
                cout << cnt << endl;
                break;
            }
            case 4: {
                if (cnt == 0) {
                    cout << 1 << endl;
                } else {
                    cout << 0 << endl;
                }
                break;
            }
            case 5: {
                int p = -1;
                if (cnt > 0) {
                    p = lst[cnt-1];                
                }
                cout << p << endl;
                break;
            }
        }
    }
    
    return 0;
}
