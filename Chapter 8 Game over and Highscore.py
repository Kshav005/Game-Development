import pygame 
import random
import os 

x = pygame.init()
snah, snaw = 25, 25


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




def gameloop() : 
    
    bground =  (192, 203, 217)
    black = (0, 0, 102)
    red = (200, 0, 0)
    snax, snay = 100, 100
    clock = pygame.time.Clock()
    velx = 0 
    vely = 0
    foodx = random.randint(0, 850)
    foody = random.randint(0, 650)
    score = 0 
    col = (0, 50, 0)
    
    exit_game = False 
    game_over = False 
    snk_list = []
    snake_length = 1 
    
    if(not os.path.exists("highscore.txt")) : 
      with open("highscore.txt", "w") as b : 
        b.write("0")
    with open("highscore.txt", "r") as f :
        high = f.read()
    
    while not exit_game :
        if game_over : 
            win.fill((255, 255, 255))
            tex("Game Over! Press Enter to continue", black, 0, 0)
            with open("highscore.txt", "w") as t: 
                t.write(str(high))
                
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RETURN : 
                        gameloop()
                        
                    if event.key == pygame.K_ESCAPE : 
                        quit()
        else : 
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_ESCAPE : 
                        quit()

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

            win.fill(bground)
            pygame.draw.rect(win, red, [foodx, foody, 15, 15])
            tex(f"Score = {score}", col, 5, 5)
            tex(f"High Score = {high}", col, 250, 5)
            if int(high) < score : 
                high = score
            else : 
                pass
            
            head = []
            head.append(snax)
            head.append(snay)    
            snk_list.append(head)

            if len(snk_list) > snake_length : 
                del snk_list[0]

            if snax < 0 or snax > 900 or snay < 0 or snay > 700 : 
                game_over = True

            if head in snk_list[:-1] :
                game_over = True
                
            
            plot(win, black, snk_list, snah)    

        pygame.display.update()
        clock.tick(60)
    
    
gameloop()
    
    
    