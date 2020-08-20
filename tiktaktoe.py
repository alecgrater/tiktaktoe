import pygame
import sys
pygame.init()

#adding comment to see if git works

#initialize the display
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Multiplayer Tik Tak Toe')

#initialize icons for both players and resize them to fit the tiles
x_Img = pygame.image.load('Player1.png')
o_Img = pygame.image.load('Player2.png')
x_Img = pygame.transform.scale(x_Img,(190,190))
o_Img = pygame.transform.scale(o_Img,(190,190))

#initialize additional needed variables
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

#defining the 9 tiles by range
range1 = range(200)
range2 = range(200,400)
range3 = range(400,600)
tiles = [[range1, range1], [range2, range1], [range3, range1],
         [range1, range2], [range2, range2], [range3, range2],
         [range1, range3], [range2, range3], [range3, range3]]

#defining the 9 tiles by their left,left coordinates
tile_values = [(5, 5),   (205, 5),   (405, 5),
              (5, 205), (205, 205), (405, 205),
              (5, 405), (205, 405), (405, 405)]

#draws a new blank board
def window_setup():
    screen.fill(white)

    #drawing vertical lines
    pygame.draw.line(screen, black, (round(width / 3), 0), (round(width / 3), height), 7)
    pygame.draw.line(screen, black, (round(width / 3 * 2), 0), (round(width / 3 * 2), height), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, black, (0, round(height / 3)), (width, round(height / 3)), 7)
    pygame.draw.line(screen, black, (0, round(height / 3 * 2)), (width, round(height / 3 * 2)), 7)

#function maintains tracking who's turn it is
def changeplayer(player):
    if player == 'player1':
        player = 'player2'
    else:
        player = 'player1'
    print('Changed the player. Current player is {}'.format(player))
    return player

#determins current player and fills their selected tile with their corresponding symbol
def filltile(tile,player):
    if player == 'player1':
        screen.blit(x_Img, tile_values[tile])
    else:
        screen.blit(o_Img, tile_values[tile])
    print('Filled the tile. Current player is {}'.format(player))
    pygame.display.update()

#when a user selects a tile, this method
def interact(player):
    print('Detected interaction. Current player is {}'.format(player))
    if pygame.mouse.get_pressed()[0] == 1:
        x_pos = pygame.mouse.get_pos()[0]
        y_pos = pygame.mouse.get_pos()[1]
        for index, tile in enumerate(tiles):
                if x_pos in tile[0] and y_pos in tile[1]:
                    clicked_tile = index
                    filltile(clicked_tile, player)
    print('Finished interaction. Current player is {}'.format(player))
    player = changeplayer(player)
    return player

#main game loop function
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
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

