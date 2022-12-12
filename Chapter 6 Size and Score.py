import pygame 
import random

x = pygame.init()

bground =  (192, 203, 217)
black = (0, 0, 102)
red = (200, 0, 0)
snax, snay, snah, snaw = 100, 100, 25, 25
clock = pygame.time.Clock()
velx = 0 
vely = 0
foodx = random.randint(0, 900)
foody = random.randint(0, 700)
score = 0 


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
            if event.key == pygame.K_ESCAPE : 
                exit_game = True
        
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_RIGHT : 
                velx = 5
                vely = 0
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT : 
                velx = -5
                vely = 0 
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_UP : 
                vely = -5
                velx = 0 
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_DOWN : 
                vely = 5 
                velx = 0
        
     
    snax = snax + velx 
    snay = snay + vely  
    
    if abs(snax - foodx) < 20 and abs(snay - foody) < 20 : 
        score += 1 
        foodx = random.randint(0, 900)
        foody = random.randint(0,700)
        snaw += 5
        print(score)  
        
    win.fill(bground)
    pygame.draw.rect(win, black, [snax, snay, snaw, snah])
    pygame.draw.rect(win, red, [foodx, foody, 15, 15])
    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    