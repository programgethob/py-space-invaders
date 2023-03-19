import pygame 
from sys import exit

pygame.init()


SIZE = [1000,1020]
#screen declare
Screen = pygame.display.set_mode(SIZE,0,32)

#image declaring 
enemy = pygame.image.load("sprites/enemy.png")
ship = pygame.image.load("sprites/ship.png")
lazer = pygame.image.load("sprites/lazer.png")

#vale declare
x=450
y=790
move_left = False
move_right=False

l = True
l2 = True
l3 = True
l4 = True
l5 = True

lazer_on_screen = False
y_lazer = y
x_lazer = x

enemy_rect=None

lazer_rect=pygame.Rect(x_lazer,y_lazer,4,14)

temp_y_lazer=y
state = True



lvl_1_enemys=((True),(True),(True),(True),(True))
lvl_1_loc_enemy=((450,500),(600,500),(300,500),(450,650),(450,350))

lvl_1_enemys = list(lvl_1_enemys)
lvl_1_loc_enemy = list(lvl_1_loc_enemy)

def enemy2(x,z,u,state):
    global enemy_rect,lazer_rect
    x1=x[0]
    y=x[1]
    if state == True:
        enemy_rect=pygame.Rect(x1,y,z,u)
        
        if pygame.Rect.colliderect(enemy_rect,lazer_rect):
            state = False
            

            return state
        else:
            return True       
    
state = True    

while True:
    


    if lazer_on_screen == True:
         y_lazer = y_lazer-2 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right=True
            if event.key == pygame.K_SPACE and lazer_on_screen == False:
                lazer_on_screen = True
                
                y_lazer = temp_y_lazer+5
                x_lazer = x+36

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right=False
        
    if lazer_on_screen:
        lazer_rect=pygame.Rect(x_lazer,y_lazer,4,14)

    if move_left == True and x != -1:
        x=x-0.25
    if move_right == True and x != 926:
        x=x+0.25
    Screen.fill((0,0,0))
    if any(lvl_1_enemys):
        if lvl_1_enemys[0]:
            Screen.blit(enemy,lvl_1_loc_enemy[0])
        if lvl_1_enemys[1]:
            Screen.blit(enemy,lvl_1_loc_enemy[1])
        if lvl_1_enemys[2]:
            Screen.blit(enemy,lvl_1_loc_enemy[2])
        if lvl_1_enemys[3]:
            Screen.blit(enemy,lvl_1_loc_enemy[3])
        if lvl_1_enemys[4]:
            Screen.blit(enemy,lvl_1_loc_enemy[4])

    Screen.blit(ship,(x,y))
    if lazer_on_screen == True and y_lazer != -31:
        Screen.blit(lazer,(x_lazer,y_lazer))
    
    if y_lazer == -31 or l == False or l2 == False or l3 == False or l4 == False or l5 == False:
        lazer_on_screen = False
        l = True
        l2 = True
        l3 = True
        l4 = True
        l5 = True
    
    temp_y_lazer=y

    if any(lvl_1_enemys):
        l =  enemy2(lvl_1_loc_enemy[0],76,56,lvl_1_enemys[0])
        l2 = enemy2(lvl_1_loc_enemy[1],76,56,lvl_1_enemys[1])
        l3 = enemy2(lvl_1_loc_enemy[2],76,56,lvl_1_enemys[2])
        l4 = enemy2(lvl_1_loc_enemy[3],76,56,lvl_1_enemys[3])
        l5 = enemy2(lvl_1_loc_enemy[4],76,56,lvl_1_enemys[4])
    
    if any(lvl_1_enemys):
        lvl_1_enemys[0] = enemy2(lvl_1_loc_enemy[0],76,56,lvl_1_enemys[0])
        lvl_1_enemys[1] = enemy2(lvl_1_loc_enemy[1],76,56,lvl_1_enemys[1])
        lvl_1_enemys[2] = enemy2(lvl_1_loc_enemy[2],76,56,lvl_1_enemys[2])
        lvl_1_enemys[3] = enemy2(lvl_1_loc_enemy[3],76,56,lvl_1_enemys[3])
        lvl_1_enemys[4] = enemy2(lvl_1_loc_enemy[4],76,56,lvl_1_enemys[4])
    if not any(lvl_1_enemys):
        pygame.quit()
        exit()
    
    pygame.display.update()
