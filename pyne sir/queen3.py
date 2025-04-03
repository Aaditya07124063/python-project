from collections import deque

def backtrack(arrangement, students, solutions):
    if not students:
        solutions.append(arrangement[:])
        return
    for i in range(len(students)):
        arrangement.append(students[i])
        backtrack(arrangement, students[:i] + students[i+1:], solutions)
        arrangement.pop()

def generate_seating_permutations():
    students = ['B1', 'B2', 'G1']
    solutions = []
    backtrack([], students, solutions)
    return solutions

def backtrack_restricted(arrangement, students, solutions):
    if not students:
        if not ('B1' in arrangement and 'B2' in arrangement and arrangement.index('G1') == (arrangement.index('B1') + arrangement.index('B2')) // 2):
            solutions.append(arrangement[:])
        return
    for i in range(len(students)):
        arrangement.append(students[i])
        backtrack_restricted(arrangement, students[:i] + students[i+1:], solutions)
        arrangement.pop()

def generate_restricted_seating():
    students = ['B1', 'B2', 'G1']
    solutions = []
    backtrack_restricted([], students, solutions)
    return solutions

def bfs_seating():
    students = ['B1', 'B2', 'G1']
    queue = deque([([], students)])
    solutions = []
    while queue:
        arrangement, remaining = queue.popleft()
        if not remaining:
            solutions.append(arrangement)
        else:
            for i in range(len(remaining)):
                queue.append((arrangement + [remaining[i]], remaining[:i] + remaining[i+1:]))
    return solutions

def bfs_restricted_seating():
    students = ['B1', 'B2', 'G1']
    queue = deque([([], students)])
    solutions = []
    while queue:
        arrangement, remaining = queue.popleft()
        if not remaining:
            if not ('B1' in arrangement and 'B2' in arrangement and arrangement.index('G1') == (arrangement.index('B1') + arrangement.index('B2')) // 2):
                solutions.append(arrangement)
        else:
            for i in range(len(remaining)):
                queue.append((arrangement + [remaining[i]], remaining[:i] + remaining[i+1:]))
    return solutions

print("All seatings:")
print(generate_seating_permutations())
print("Restricted seatings:")
print(generate_restricted_seating())
print("BFS All seatings:")
print(bfs_seating())
print("BFS Restricted seatings:")
print(bfs_restricted_seating())
