import pygame 

pygame.init()
screen = pygame.display.set_mode((800,800))

exit = False


keys = [False , False]

#player structure 
player_x = 400
player_y = 600
player_width = 100
player_height = 10
#ball stuff 
ball_x = 400
ball_y = 400
#ball vel
vx = 1
vy = 1
clock = pygame.time.Clock()

p_rect = pygame.rect.Rect(player_x, player_y, player_width, player_height)
ball_rect = pygame.rect.Rect(400,400, 10,10 )
if "__main__":
    pass
    while exit is False:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type  ==pygame.QUIT:
                
                exit = True
            if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_a:
                    keys[0]=True
                elif event.key == pygame.K_d:
                    keys[1]=True
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    keys[0]=False
                elif event.key == pygame.K_d:
                    keys[1]=False
        pass
        #logic/math stuff here
        if keys[0] == True:
            
            p_rect.x -=2 
        if keys[1] == True:
            p_rect.x+=2
        pass# do nothing if neither are true 
        
        ball_rect.x += vx
        ball_rect.y +=vy
        if  ball_rect.colliderect(p_rect) is True:
            
            vx *=-1
            vy*=-1
        if ball_rect.x <= 0 or ball_rect.x+ball_rect.width >=800:
            
            vx *=-1
        if ball_rect.y <=0 or ball_rect.y + ball_rect.height >= 800:
            
            vy *=-1
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (0, 0, 255),
                 p_rect, 2)
        pygame.draw.rect(screen,(0,0,255), ball_rect, 2 )
        pygame.display.update()

        
