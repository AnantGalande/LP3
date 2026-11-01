// Fibonacci Series - Recursive and Iterative
#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1)
        return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Recursive: O(2^n) time, O(n) space
void recursive(int n) {
    for (int i = 0; i < n; i++)
        cout << fibonacci(i) << " ";
    cout << endl;
}

// Iterative: O(n) time, O(1) space
void iterative(int n) {
    int a1 = 0, a2 = 1;

    for (int i = 0; i < n; i++) {
        cout << a1 << " ";

        int a3 = a1 + a2;
        a1 = a2;
        a2 = a3;
    }
    cout << endl;
}

int main() {
    recursive(10);
    iterative(10);
    return 0;
}