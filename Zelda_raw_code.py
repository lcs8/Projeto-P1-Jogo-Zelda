import pygame
import os
import random
pygame.init()
pygame.display.set_caption("zelda clone")
#Int Variables
WIDTH = 1080
HEIGHT = 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
FPS = 60
SPRITES_WIDTH, SPRITES_HEIGHT = 50, 70
VEL = 5
#Sprites Variables
LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'down.png'))
LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
RUPEE_IMAGE = pygame.image.load(os.path.join('assets', 'red_rupee.png'))
RUPEE = pygame.transform.scale(RUPEE_IMAGE,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
BACKGROUND = pygame.image.load(os.path.join('assets', 'bg.jpg'))
ARROW_IMAGE = pygame.image.load(os.path.join('assets','Arrow.png'))
ARROW = pygame.transform.scale(ARROW_IMAGE,(SPRITES_HEIGHT- 20 ,SPRITES_HEIGHT- 20))
HEARTH_IMAGE = pygame.image.load(os.path.join('assets','Hearth.png'))
HEARTH = pygame.transform.scale(HEARTH_IMAGE,(SPRITES_HEIGHT - 30 ,SPRITES_HEIGHT - 30))
#Funcion that prints everything on the window
def draw_window(sprite,font,Rupee,RUPEES_COLECTED,Rupee_Color,keys_pressed,arrow,ARROWS,Hearth,HEARTHS):
    WINDOW.fill(WHITE)
    WINDOW.blit(BACKGROUND,(0, 0))
    if keys_pressed[pygame.K_w]:
            LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'up.png'))
            LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
            WINDOW.blit(LINK,(sprite.x,sprite.y))
            
            
    elif keys_pressed[pygame.K_s]:
            LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'down.png'))
            LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
            WINDOW.blit(LINK,(sprite.x,sprite.y))
        
    elif keys_pressed[pygame.K_a]:
            LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'left.png'))
            LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
            WINDOW.blit(LINK,(sprite.x,sprite.y))
        
    elif keys_pressed[pygame.K_d]:
            LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'Right.png'))
            LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
            WINDOW.blit(LINK,(sprite.x,sprite.y))
        
            
    else:
         LINK_IMAGE = pygame.image.load(os.path.join('assets','links sprites', 'down.png'))
         LINK = pygame.transform.scale(LINK_IMAGE,(SPRITES_WIDTH,SPRITES_HEIGHT))
         WINDOW.blit(LINK,(sprite.x,sprite.y))
         
    if Rupee_Color < 70:
        RUPEE_IMAGE = pygame.image.load(os.path.join('assets', 'green_rupee.png'))
        RUPEE = pygame.transform.scale(RUPEE_IMAGE,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
    elif Rupee_Color >= 70 and Rupee_Color < 90:
        RUPEE_IMAGE = pygame.image.load(os.path.join('assets', 'blue_rupee.png'))
        RUPEE = pygame.transform.scale(RUPEE_IMAGE,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
    elif Rupee_Color >= 90:
        RUPEE_IMAGE = pygame.image.load(os.path.join('assets', 'red_rupee.png'))
        RUPEE = pygame.transform.scale(RUPEE_IMAGE,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
    WINDOW.blit(RUPEE,(Rupee.x,Rupee.y))
    score_text = font.render(f'Rupees: {RUPEES_COLECTED}', True, (255, 255, 255))
    arrow_text = font.render(f'Arrows: {ARROWS}', True, (255, 255, 255))
    Hearth_text = font.render(f'HP: {HEARTHS}', True, (255, 255, 255))
    WINDOW.blit(ARROW,(arrow.x,arrow.y))
    WINDOW.blit(HEARTH,(Hearth.x,Hearth.y))
    WINDOW.blit(score_text, (10, 10))
    WINDOW.blit(arrow_text, (10, 60))
    WINDOW.blit(Hearth_text, (10, 110))
    pygame.display.update()

#Funcion responsible for links movement
def link_movement(keys_pressed,link):
    if keys_pressed[pygame.K_w] and link.y - VEL > 0 : #Up
        link.y -= VEL
    if keys_pressed[pygame.K_s]and link.y + VEL + link.height < HEIGHT : #Down
        link.y += VEL 
    if keys_pressed[pygame.K_a]and link.x - VEL > 0: #Left
        link.x -= VEL
    if keys_pressed[pygame.K_d]and link.x + VEL + link.width < WIDTH: #Right
        link.x += VEL           

#Main function
def main():
    Rupee_Color = 0
    RUPEES_COLECTED = 0
    ARROWS = 0 
    HEARTHS = 3
    font = pygame.font.Font(os.path.join('assets', 'Roboto-Black.ttf'), 40)
    link = pygame.Rect(300, 100, SPRITES_WIDTH, SPRITES_HEIGHT)
    Rupee = pygame.Rect(500, 200,SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
    arrow = pygame.Rect(400, 300,SPRITES_WIDTH/2 - 20, SPRITES_HEIGHT/2 - 20)
    Hearth = pygame.Rect(500, 600,SPRITES_WIDTH/2 - 30, SPRITES_HEIGHT/2 - 30)
    clock = pygame.time.Clock()
    running = True
    while running == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_pressed = pygame.key.get_pressed()
        link_movement(keys_pressed, link)
        if link.colliderect(Rupee):
            if Rupee_Color < 70:
                RUPEES_COLECTED += 1
                Rupee = pygame.Rect(random.randint(0,WIDTH - 100), random.randint(0,HEIGHT - 100),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                Rupee_Color = random.randint(0,100)
            elif Rupee_Color >= 70 and Rupee_Color < 90:
                RUPEES_COLECTED += 5
                Rupee = pygame.Rect(random.randint(0,WIDTH- 100), random.randint(0,HEIGHT- 100),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                Rupee_Color = random.randint(0,100)
            elif Rupee_Color >= 90:
                RUPEES_COLECTED += 20
                Rupee = pygame.Rect(random.randint(0,WIDTH- 100) - 10, random.randint(0,HEIGHT- 100) - 10,SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                Rupee_Color = random.randint(0,100)    
            
        if link.colliderect(arrow):
            ARROWS += 1
            arrow = pygame.Rect(random.randint(0,WIDTH - 100), random.randint(0,HEIGHT - 100),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
        if link.colliderect(Hearth) and HEARTHS < 5:
            HEARTHS += 1
            Hearth = pygame.Rect(random.randint(0,WIDTH - 100), random.randint(0,HEIGHT- 100),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
            

        draw_window(link,font,Rupee,RUPEES_COLECTED,Rupee_Color,keys_pressed,arrow,ARROWS,Hearth,HEARTHS)
    pygame.quit()

if __name__ == "__main__":
    main()