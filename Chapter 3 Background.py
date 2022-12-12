import pygame 


x = pygame.init()

bground =  (192, 203, 217)
black = (0, 0, 102)
snax, snay, snah, snaw = 50, 50, 15, 15

win = pygame.display.set_mode((900,700))
pygame.display.set_caption("Something, I don't know")
pygame.display.update()

exit_game = False 
game_over = False 

while not exit_game : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            exit_game = True
        
    # for backgroud color, works in rgb values 
    win.fill(bground)
    
    # used to draw a rectangle (surface, color, [x, y, width, height])
    pygame.draw.rect(win, black, [snax, snay, snaw, snah] )
    
    # needs to be run again and again if window attributes are edited
    pygame.display.update()
    
    
    