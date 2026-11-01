#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

int partition(vector<int>& a, int low, int high, bool random) {

    if(random) {
        int r = low + rand() % (high - low + 1);
        swap(a[low], a[r]);
    }

    int pivot = a[low];
    int i = low + 1;
    int j = high;

    while(i <= j) {

        while(i <= high && a[i] <= pivot)
            i++;

        while(a[j] > pivot)
            j--;

        if(i < j)
            swap(a[i], a[j]);
    }

    swap(a[low], a[j]);
    return j;
}

void quickSort(vector<int>& a, int low, int high, bool random) {

    if(low < high) {

        int p = partition(a, low, high, random);

        quickSort(a, low, p - 1, random);
        quickSort(a, p + 1, high, random);
    }
}

int main() {

    int n, ch;
    cout << "Enter size: ";
    cin >> n;

    vector<int> a(n);

    cout << "Enter elements: ";
    for(int i = 0; i < n; i++)
        cin >> a[i];

    cout << "1. Deterministic  2. Randomized: ";
    cin >> ch;

    srand(time(0));

    quickSort(a, 0, n - 1, ch == 2);

    cout << "Sorted array: ";
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}