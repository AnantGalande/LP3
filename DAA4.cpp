#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isSafe(vector<int>& board, int row, int col) {
    for(int i = 0; i < col; i++) {
        if(board[i] == row ||
           abs(board[i] - row) == abs(i - col)) {
            return false;
        }
    }
    return true;
}

bool solveNQueens(vector<int>& board, int col, int n) {
    if(col == n)
        return true;

    for(int row = 0; row < n; row++) {
        if(isSafe(board, row, col)) {
            board[col] = row;

            if(solveNQueens(board, col + 1, n))
                return true;

            board[col] = -1;
        }
    }

    return false;
}

void printBoard(vector<int>& board, int n) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(board[j] == i)
                cout << "Q ";
            else
                cout << ". ";
        }
        cout << endl;
    }
}

int main() {
    int n;

    cout << "Enter board size: ";
    cin >> n;

    if(n <= 0) {
        cout << "Invalid board size";
        return 0;
    }

    vector<int> board(n, -1);

    // Place first queen at row 0, column 0
    board[0] = 0;

    // Start placing queens from column 1
    if(solveNQueens(board, 1, n)) {
        cout << "\nSolution:\n";
        printBoard(board, n);
    }
    else {
        cout << "Solution does not exist";
    }

    return 0;
}