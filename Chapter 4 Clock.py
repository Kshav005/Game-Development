import pygame 


x = pygame.init()

bground =  (192, 203, 217)
black = (0, 0, 102)
snax, snay, snah, snaw = 100, 100, 15, 15

# Python real time clock 
clock = pygame.time.Clock()


win = pygame.display.set_mode((900,700))
pygame.display.set_caption("Something, I don't know")
pygame.display.update()

exit_game = False 
game_over = False 

while not exit_game : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            exit_game = True
        
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_RIGHT : 
                snax = snax + 10 
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT : 
                snax = snax - 10 
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_UP : 
                snay = snay - 10 
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_DOWN : 
                snay = snay + 10 
        
        
    win.fill(bground)
    pygame.draw.rect(win, black, [snax, snay, snaw, snah] )
    pygame.display.update()
    
    # Clock with FPS
    clock.tick(30)
    
    
    
    
    
    
    
    
    