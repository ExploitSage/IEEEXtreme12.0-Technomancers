from sys import stdin

def coord_to_space(col, row, size):
    if col == 0:
        if row == 1:
            return 0
        elif row == size:
            return (pow(size, 2)+1)
    
    space = (row-1)*size
    if row % 2 == 0:
        space += size-(col-1)
    else:
        space += col
    return space

def space_to_coord(space, size):
    if space == 0:
        return 0, 1
    elif space >= pow(size, 2)+1:
        return 0, size
    else:
        row = ((space-1)//(size))+1
        col = ((space-1)%size)+1
        return col, row

data = [line.strip('\r\n') for line in stdin.readlines()]

board_size = int(data.pop(0).strip())

num_players = int(data.pop(0).strip())
players = [0 for i in range(0, num_players)]
players_status = [0 for i in range(0, num_players)]
current_player = 0

jump_starts = []
jump_ends = []

num_snakes = int(data.pop(0).strip())
for i in range(0, num_snakes):
    snake = data.pop(0).split()
    snake_start = coord_to_space(int(snake[0]), int(snake[1]), board_size)
    snake_end = coord_to_space(int(snake[2]), int(snake[3]), board_size)
    
    for idx, jump_end in enumerate(jump_ends):
        if snake_start == jump_end:
            jump_ends[idx] = snake_end
    
    if snake_end in jump_starts:
        snake_end = jump_ends[jump_starts.index(snake_end)]
    
    jump_starts.append(snake_start)
    jump_ends.append(snake_end)

num_ladders = int(data.pop(0).strip())
for i in range(0, num_ladders):
    ladder = data.pop(0).split()
    ladder_start = coord_to_space(int(ladder[0]), int(ladder[1]), board_size)
    ladder_end = coord_to_space(int(ladder[2]), int(ladder[3]), board_size)
    
    for idx, jump_end in enumerate(jump_ends):
        if ladder_start == jump_end:
            jump_ends[idx] = ladder_end
    
    if ladder_end in jump_starts:
        ladder_end = jump_ends[jump_starts.index(ladder_end)]
    
    jump_starts.append(ladder_start)
    jump_ends.append(ladder_end)

num_rolls = int(data.pop(0).strip())
rolls = [sum([int(j) for j in roll.split()]) for roll in data]

for roll in rolls:
    players[current_player] += roll
    if players[current_player] in jump_starts:
        players[current_player] = jump_ends[jump_starts.index(players[current_player])]
    if players[current_player] >= (pow(board_size,2)+1):
        players_status[current_player] = 1
        if sum(players_status) == num_players:
            break
    current_player = (current_player+1)%num_players
    while players_status[current_player] == 1:
        current_player = (current_player+1)%num_players

for i in range(0, num_players):
    if players_status[i] == 1:
        print("%i winner" % (i+1))
    else:
        col, row = space_to_coord(players[i], board_size)
        print("%i %i %i" % (i+1, col, row))