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
VEL = 7
BACKGROUND = pygame.image.load(os.path.join('assets', 'bg.jpg'))

class Player():
    def __init__(self):
        self.Sprites = [pygame.image.load(os.path.join('assets','links sprites', 'down.png')),
                         pygame.image.load(os.path.join('assets','links sprites', 'up.png')),
                         pygame.image.load(os.path.join('assets','links sprites', 'left.png')),
                         pygame.image.load(os.path.join('assets','links sprites', 'Right.png'))
                        ]
        self.imagem = self.Sprites[0]
        self.imagem = pygame.transform.scale(self.imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        self.Rect = pygame.Rect(300, 100, SPRITES_WIDTH, SPRITES_HEIGHT)
        self.x, self.y = 300, 100
        WINDOW.blit(self.imagem,(self.x, self.y))
    def link_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.y - VEL > 0 : #Up
            self.y -= VEL
            self.imagem = self.Sprites[1]
            self.imagem = pygame.transform.scale(self.imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        if keys_pressed[pygame.K_s] and self.y + VEL + self.Rect.height < HEIGHT : #Down
            self.y += VEL 
            self.imagem = self.Sprites[0]
            self.imagem = pygame.transform.scale(self.imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        if keys_pressed[pygame.K_a] and self.x - VEL > 0: #Left
            self.x -= VEL
            self.imagem = self.Sprites[2]
            self.imagem = pygame.transform.scale(self.imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        if keys_pressed[pygame.K_d] and self.x + VEL +self.Rect.width < WIDTH: #Right
            self.x += VEL  
            self.imagem = self.Sprites[3]
            self.imagem = pygame.transform.scale(self.imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        self.Rect.x = self.x
        self.Rect.y = self.y

    
class Item():
    def __init__(self,):
        self.Sprites = [pygame.image.load(os.path.join('assets','green_rupee.png')),
                         pygame.image.load(os.path.join('assets','blue_rupee.png')),
                         pygame.image.load(os.path.join('assets','red_rupee.png')),
                         pygame.image.load(os.path.join('assets','Arrow.png')),
                         pygame.image.load(os.path.join('assets','Hearth.png'))
                        ]
    def Rupee(self,rupee_value):
        
        self.rupee_color = rupee_value
        if self.rupee_color < 70:
            self.rupee_imagem = self.Sprites[0]
        elif self.rupee_color >= 70 and self.rupee_color < 90:
            self.rupee_imagem = self.Sprites[1]
        elif self.rupee_color >= 90:
            self.rupee_imagem = self.Sprites[2]

        self.rupee_imagem = pygame.transform.scale(self.rupee_imagem,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
        self.rupee_x , self.rupee_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.rupee_rect = pygame.Rect(self.rupee_x, self.rupee_y, SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
        self.rupee_rect.x = self.rupee_x
        self.rupee_rect.y = self.rupee_y
    def Arrow(self):
        self.arrow_imagem = self.Sprites[3]
        self.arrow_imagem = pygame.transform.scale(self.arrow_imagem,(SPRITES_WIDTH,SPRITES_HEIGHT))
        self.arrow_x, self.arrow_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.arrow_rect = pygame.Rect(self.arrow_x, self.arrow_y, SPRITES_WIDTH, SPRITES_HEIGHT)
        self.arrow_rect.x = self.arrow_x
        self.arrow_rect.y = self.arrow_y
    def Hearth(self):
        self.hearth_imagem = self.Sprites[4]
        self.hearth_imagem = pygame.transform.scale(self.hearth_imagem,(SPRITES_WIDTH/2,SPRITES_HEIGHT/2))
        self.hearth_x, self.hearth_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.hearth_rect = pygame.Rect(self.hearth_x, self.hearth_y, SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
        self.hearth_rect.x = self.hearth_x
        self.hearth_rect.y = self.hearth_y




        
         


def main():
    HEARTHS = 3
    RUPEES_COLECTED = 0
    ARROWS_COLECTED = 0
    rupee_color = 0
    font = pygame.font.Font(os.path.join('assets', 'Roboto-Black.ttf'), 40)
    clock = pygame.time.Clock()
    player = Player()
    itens = Item()
    itens.Rupee(rupee_color)
    itens.Arrow()
    itens.Hearth()
    running = True
    while running == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_pressed = pygame.key.get_pressed()
        WINDOW.blit(BACKGROUND,(0, 0))
        
        player.link_movement(keys_pressed)
        WINDOW.blit(player.imagem, (player.x, player.y))
        WINDOW.blit(itens.rupee_imagem,(itens.rupee_rect.x,itens.rupee_rect.y))
        WINDOW.blit(itens.arrow_imagem,(itens.arrow_rect.x,itens.arrow_rect.y))
        WINDOW.blit(itens.hearth_imagem,(itens.hearth_rect.x,itens.hearth_rect.y))
        if player.Rect.colliderect(itens.rupee_rect):
            if itens.rupee_color < 70:
                RUPEES_COLECTED += 1
                itens.rupee_rect = pygame.Rect(random.randint(0,WIDTH), random.randint(0,HEIGHT),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
            elif itens.rupee_color >= 70 and itens.rupee_color < 90:
                RUPEES_COLECTED += 5
                itens.rupee_rect = pygame.Rect(random.randint(0,WIDTH), random.randint(0,HEIGHT),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
            elif itens.rupee_color >= 90:
                RUPEES_COLECTED += 20
                itens.rupee_rect = pygame.Rect(random.randint(0,WIDTH - 100), random.randint(0,HEIGHT),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
        if player.Rect.colliderect(itens.arrow_rect):    
            ARROWS_COLECTED += 1
            itens.arrow_rect = pygame.Rect(random.randint(0,WIDTH), random.randint(0,HEIGHT),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
            itens.Arrow()
        if player.Rect.colliderect(itens.hearth_rect):    
            HEARTHS += 1
            itens.hearth_rect = pygame.Rect(random.randint(0,WIDTH), random.randint(0,HEIGHT),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
            itens.Hearth()
        score_text = font.render(f'Rupees: {RUPEES_COLECTED}', True, (255, 255, 255))
        WINDOW.blit(score_text, (10, 10))
        arrow_text = font.render(f'Arrows: {ARROWS_COLECTED}', True, (255, 255, 255))
        WINDOW.blit(arrow_text, (10, 60))
        hearth_text = font.render(f'HP: {HEARTHS}', True, (255, 255, 255))
        WINDOW.blit(hearth_text, (10,110))
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()