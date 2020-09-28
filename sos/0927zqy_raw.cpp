# include <iostream>

using namespace std;

int main(){
    // cin >> n;
    char arr[] = "EEEEEEFFFFFF";
    // for (int k = 0; k < n; k++) {
    //     cin >> arr[k];s
    // }
    int b = 0;
    int n = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < n; i ++) {
        int a = 0;
        for (int j = i; j < n; j++) {
            if (arr[j] == 'E') {
                a++;
            } else {
                a--;
            }
            b = max(abs(a), b);
        }
    }
    cout << b << endl;
    return 0;
}