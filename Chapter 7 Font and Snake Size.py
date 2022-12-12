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
col = (0, 50, 0)


# Changing font
pygame.font.get_fonts()
font = pygame.font.SysFont('arialblack', 40)

def tex(text, color, x, y) : 
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x,y])

# Creating fuction to increase the size of the snake 
def plot(win, color, snk_list, snah) :
    for x,y in snk_list : 
        pygame.draw.rect(win, color, [x, y, snaw, snah])






win = pygame.display.set_mode((900,700))
pygame.display.set_caption("Something, I don't know")
pygame.display.update()

exit_game = False 
game_over = False 

# Creating a default list 
snk_list = []
snake_length = 1

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
        snake_length += 5
        
        # Increasing snake size while it eats a food item 
        snake_length += 5
        
    win.fill(bground)
    pygame.draw.rect(win, red, [foodx, foody, 15, 15])
    tex(f"Score = {score}", col, 5, 5)
    
    
    # default size 
    head = []
    head.append(snax)
    head.append(snay)    
    snk_list.append(head)
    
    if len(snk_list) > snake_length : 
        del snk_list[0]
    
    # Using function to plot the snake properly
    plot(win, black, snk_list, snah)    
    
    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
    