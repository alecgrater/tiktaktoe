import pygame
import sys

# Initialize pygame
pygame.init()

# Initialize the display
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Multiplayer Tic Tac Toe')

# Initialize icons for both players and resize them to fit the tiles
x_Img = pygame.image.load('Player1.png')
o_Img = pygame.image.load('Player2.png')
x_Img = pygame.transform.scale(x_Img, (190, 190))
o_Img = pygame.transform.scale(o_Img, (190, 190))

# Initialize additional needed variables
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Define the 9 tiles by range
ranges = [range(200), range(200, 400), range(400, 600)]
tiles = [[(x, y) for x in r] for y in r]

# Define the 9 tiles by their top-left coordinates
tile_values = [(5, 5), (205, 5), (405, 5),
               (5, 205), (205, 205), (405, 205),
               (5, 405), (205, 405), (405, 405)]


# Draw a new blank board
def window_setup():
    screen.fill(white)

    # Draw vertical lines
    pygame.draw.line(screen, black, (round(width / 3), 0), (round(width / 3), height), 7)
    pygame.draw.line(screen, black, (round(width / 3 * 2), 0), (round(width / 3 * 2), height), 7)

    # Draw horizontal lines
    pygame.draw.line(screen, black, (0, round(height / 3)), (width, round(height / 3)), 7)
    pygame.draw.line(screen, black, (0, round(height / 3 * 2)), (width, round(height / 3 * 2)), 7)


# Function to change the current player
def change_player(player):
    if player == 'player1':
        player = 'player2'
    else:
        player = 'player1'
    print('Changed the player. Current player is {}'.format(player))
    return player


# Fill the selected tile with the corresponding player's symbol
def fill_tile(tile, player):
    if player == 'player1':
        screen.blit(x_Img, tile_values[tile])
    else:
        screen.blit(o_Img, tile_values[tile])
    print('Filled the tile. Current player is {}'.format(player))
    pygame.display.update()


# Handle player interaction when selecting a tile
def interact(player):
    print('Detected interaction. Current player is {}'.format(player))
    if pygame.mouse.get_pressed()[0] == 1:
        x_pos, y_pos = pygame.mouse.get_pos()
        for index, tile in enumerate(tiles):
            if x_pos in tile[0] and y_pos in tile[1]:
                clicked_tile = index
                fill_tile(clicked_tile, player)
    print('Finished interaction. Current player is {}'.format(player))
    player = change_player(player)
    return player


# Main game loop function
def main():
    clock = pygame.time.Clock()
    window_setup()
    player = 'player1'
    print('Started game. Current player is {}'.format(player))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player = interact(player)
        clock.tick(15)
        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.quit()
sys.exit()
