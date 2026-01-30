
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int N = 8;
vector<int> board(N, -1); // board[row] = column

// Check if a queen can be placed at board[row][col]
bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++) {
        // Same column or diagonal check
        if (board[i] == col || abs(board[i] - col) == abs(i - row))
            return false;
    }
    return true;
}

// Print current board state
void printBoard() {
    cout << "\nFinal Chessboard Configuration:\n\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i] == j)
                cout << " Q ";
            else
                cout << " . ";
        }
        cout << endl;
    }
}

// Backtracking function
bool solveNQueens(int row) {
    if (row == N) {
        return true; // All queens placed
    }

    for (int col = 0; col < N; col++) {
        cout << "Trying to place Queen at Row " << row + 1
             << ", Column " << col + 1 << endl;

        if (isSafe(row, col)) {
            board[row] = col;
            cout << "✔ Queen placed at Row " << row + 1
                 << ", Column " << col + 1 << endl;

            if (solveNQueens(row + 1))
                return true;

            // Backtracking
            board[row] = -1;
            cout << "✘ Backtracking from Row " << row + 1
                 << ", Column " << col + 1 << endl;
        }
    }
    return false;
}

int main() {
    cout << "8-Queens Problem using Backtracking (C++)\n";
    cout << "-----------------------------------------\n";

    if (solveNQueens(0)) {
        printBoard();
    } else {
        cout << "No solution exists.\n";
    }

    return 0;
}
