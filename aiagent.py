import pygame, sys, math, time

# --- Setup ---
WIDTH, ROWS = 600, 3
SQ = WIDTH // ROWS
board = [[0] * ROWS for _ in range(ROWS)] # 0=Empty, 1=Human(X), 2=AI(O)

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))

def draw():
    screen.fill((28, 170, 156))
    # Draw Grid
    for i in range(1, ROWS):
        pygame.draw.line(screen, (23, 145, 135), (0, i * SQ), (WIDTH, i * SQ), 10)
        pygame.draw.line(screen, (23, 145, 135), (i * SQ, 0), (i * SQ, WIDTH), 10)
    # Draw X and O
    for r in range(ROWS):
        for c in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.line(screen, (84, 84, 84), (c*SQ+40, r*SQ+40), (c*SQ+SQ-40, r*SQ+SQ-40), 15)
                pygame.draw.line(screen, (84, 84, 84), (c*SQ+40, r*SQ+SQ-40), (c*SQ+SQ-40, r*SQ+40), 15)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, (239, 231, 200), (c*SQ+SQ//2, r*SQ+SQ//2), SQ//3, 15)
    pygame.display.update()

# --- Game Logic ---
def check_win(p):
    for i in range(ROWS): # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] == p or board[0][i] == board[1][i] == board[2][i] == p: return True
    # Check diagonals
    return board[0][0] == board[1][1] == board[2][2] == p or board[2][0] == board[1][1] == board[0][2] == p

def is_full(): return all(board[r][c] != 0 for r in range(ROWS) for c in range(ROWS))

# --- AI Core ---
def minimax(depth, is_max, alpha, beta):
    if check_win(2): return 10 - depth  # AI wins
    if check_win(1): return depth - 10  # Human wins
    if is_full(): return 0              # Draw

    best = -math.inf if is_max else math.inf
    for r in range(ROWS):
        for c in range(ROWS):
            if board[r][c] == 0:
                board[r][c] = 2 if is_max else 1
                score = minimax(depth + 1, not is_max, alpha, beta)
                board[r][c] = 0 # Undo move
                
                if is_max:
                    best = max(best, score)
                    alpha = max(alpha, best)
                else:
                    best = min(best, score)
                    beta = min(beta, best)
                if beta <= alpha: break # Alpha-Beta Pruning
    return best

# --- Main Loop ---
draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            r, c = event.pos[1] // SQ, event.pos[0] // SQ
            if board[r][c] == 0:
                board[r][c] = 1 # Human moves
                draw()
                
                if check_win(1): print("Human Wins! (Wait, how?!)")
                elif is_full(): print("It's a Draw!")
                else:
                    # AI moves
                    t0 = time.time()
                    best_score, move = -math.inf, None
                    for i in range(ROWS):
                        for j in range(ROWS):
                            if board[i][j] == 0:
                                board[i][j] = 2
                                score = minimax(0, False, -math.inf, math.inf)
                                board[i][j] = 0
                                if score > best_score: best_score, move = score, (i, j)
                    
                    if move: board[move[0]][move[1]] = 2
                    print(f"AI Move Time: {(time.time()-t0)*1000:.1f}ms")
                    draw()
                    
                    if check_win(2): print("AI Wins! Flawless Victory.")
                    elif is_full(): print("It's a Draw!")