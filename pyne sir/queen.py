def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    backtrack(0)
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for r in range(n):
            row_str = ['▢'] * n
            row_str[sol[r]] = 'Q'
            print(' '.join(row_str))
        print()

n_values = [4, 8, 16]
for n in n_values:
    solutions = solve_n_queens(n)
    print(f"Solutions for N={n}: {len(solutions)}")
    if n == 4:
        print_solutions(solutions, n)
