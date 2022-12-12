import pygame 
import random
import os 
import time



x = pygame.init()
pygame.mixer.init()
snah, snaw = 25, 25
clock = pygame.time.Clock()

pygame.font.get_fonts()
font = pygame.font.SysFont('arialblack', 30)

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


# Adding a background 
bg = pygame.image.load("bgimg1.jpg")
bg = pygame.transform.scale(bg, (1200, 700)).convert_alpha()
bg2 = pygame.image.load("bgimg.jpg")
bg2 = pygame.transform.scale(bg2, (1200, 700)).convert_alpha()
start = pygame.image.load("load.png")
start = pygame.transform.scale(start, (370,40)).convert_alpha()
start2 = pygame.image.load("welcome.png")
start2 = pygame.transform.scale(start2, (800, 70))

def loadsc() :
    exit_game = False
    pygame.mixer.music.load("game sound.mp3")
    pygame.mixer.music.play()
    while not exit_game :     
        win.fill((0, 255, 0))
        win.blit(bg2, (0,0))
        win.blit(start, (250, 450))
        win.blit(start2, (600, 930))
        pygame.draw.rect(win, (0, 100, 250), [200, 100, 20, 20]) 
        pygame.display.flip()
        win.blit(start2, (60, 330))
        
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_SPACE :    
                    exit_game = True  
                    gameloop()
                elif event.key == pygame.K_ESCAPE : 
                    quit()
            
        pygame.display.update()
        clock.tick(60)

def gameloop() : 
    bground =  (192, 203, 217)
    white = (255, 255, 255)
    foodcol = (255, 102, 102)
    snax, snay = 100, 100
    velx = 0 
    vely = 0
    foodx = random.randint(0, 650)
    foody = random.randint(0, 650)
    score = 0 
    col = (255, 229, 204)
    exit_game = False 
    game_over = False 
    snk_list = []
    snake_length = 1 

    # Adding a good music
    pygame.mixer.music.load("ingame music.mp3")
    pygame.mixer.music.play()
    
    if(not os.path.exists("highscore.txt")) : 
      with open("highscore.txt", "w") as b : 
        b.write("0")
    with open("highscore.txt", "r") as f :
        high = f.read()
    
    while not exit_game :
        if game_over : 
            win.fill((255, 255, 255))
            win.blit(bg, (0,0))
            tex("Game Over! Press Enter to continue", white, 150, 200)
            tex(f"Your Score was : {score}", white, 150, 400)
            tex(f"Highscore : {high}", white, 150, 350)
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
            win.blit(bg, (0,0))
            pygame.draw.rect(win, foodcol, [foodx, foody, 15, 15])
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
                
            
            plot(win, white, snk_list, snah)    

        pygame.display.update()
        clock.tick(60)
    
loadsc()
    
    
    