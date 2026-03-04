import random

def generate_map(size):
    map_data = [['.' for _ in range(size)] for _ in range(size)]
    return map_data


def place_runes(map_data, num_runes):
    size = len(map_data)
    runes_placed = 0
    while runes_placed < num_runes:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if map_data[x][y] == '.':
            map_data[x][y] = 'R'
            runes_placed += 1
    return map_data


def print_map(map_data, player_x, player_y):
    size = len(map_data)
    for i in range(size):
        for j in range(size):
            if i == player_x and j == player_y:
                print('P', end='')
            else:
                print(map_data[i][j], end='')
        print()


def get_valid_input():
    while True:
        move = input("Move (w/a/s/d): ").lower()
        if move in ['w', 'a', 's', 'd']:
            return move
        else:
            print("Invalid input. Use w, a, s, or d.")



def main():
    map_size = 5
    num_runes = 3

    game_map = generate_map(map_size)
    game_map = place_runes(game_map, num_runes)

    player_x = 0
    player_y = 0
    runes_found = 0

    while runes_found < num_runes:
        print_map(game_map, player_x, player_y)
        move = get_valid_input()

        new_x, new_y = player_x, player_y
        if move == 'w':
            new_x -= 1
        elif move == 's':
            new_x += 1
        elif move == 'a':
            new_y -= 1
        elif move == 'd':
            new_y += 1

        if 0 <= new_x < map_size and 0 <= new_y < map_size:
            player_x, player_y = new_x, new_y

            if game_map[player_x][player_y] == 'R':
                print("You found a rune!")
                game_map[player_x][player_y] = '.'  # Remove the rune from the map
                runes_found += 1
        else:
            print("You can't move that way!")

    print("Congratulations! You found all the runes!")


if __name__ == "__main__":
    main()
