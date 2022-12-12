import pygame 

x = pygame.init()
wind = pygame.display.set_mode((500,500))

exit_game = False 

while not exit_game : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            exit_game = True 
    
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_3 : 
                print("You pressed 3 key!")
        
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_UP : 
                print("You pressed up key!")
        
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_w : 
                print("You pressed w key!")