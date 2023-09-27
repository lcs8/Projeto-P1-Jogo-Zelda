import pygame
import os
import random

pygame.init()
pygame.display.set_caption("Zelda Arcade")

#Int Variables
WIDTH = 1511
HEIGHT = 850
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
FPS = 60
SPRITES_WIDTH, SPRITES_HEIGHT = 90, 90
VEL = 5
BACKGROUND = pygame.image.load(os.path.join('sprits', 'bg.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, [WIDTH,HEIGHT])


class Player():
    def __init__(self):
        self.Sprites = [pygame.image.load(os.path.join('sprits','links sprites', 'down.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','links sprites', 'up.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','links sprites', 'left.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','links sprites', 'Right.png')).convert_alpha()
                        ]
        pygame.mixer.music.set_volume(0.3)
        self.music_back = pygame.mixer.music.load(os.path.join('sprits', 'BGM1.mid'))
        pygame.mixer.music.play()
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
        self.Sprites = [pygame.image.load(os.path.join('sprits','yellow_rupee.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','blue_rupee.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','red_rupee.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','Arrow.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','Hearth.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','enemy1.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','enemy2.png')).convert_alpha(),
                         pygame.image.load(os.path.join('sprits','enemy3.png')).convert_alpha()
                        ]
    def Rupee(self,rupee_value):
        self.rupee_color = rupee_value
        if self.rupee_color < 70:
            self.rupee_imagem = self.Sprites[0]
        elif self.rupee_color >= 70 and self.rupee_color < 90:
            self.rupee_imagem = self.Sprites[1]
        elif self.rupee_color >= 90:
            self.rupee_imagem = self.Sprites[2]

        self.rupee_imagem = pygame.transform.scale(self.rupee_imagem,(30, 50))
        self.rupee_x , self.rupee_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.rupee_rect = pygame.Rect(self.rupee_x, self.rupee_y, 30, 50)
        self.rupee_rect.x = self.rupee_x
        self.rupee_rect.y = self.rupee_y
    def Arrow(self):
        self.arrow_imagem = self.Sprites[3]
        self.arrow_imagem = pygame.transform.scale(self.arrow_imagem,(60, 60))
        self.arrow_x, self.arrow_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.arrow_rect = pygame.Rect(self.arrow_x, self.arrow_y, 60, 60)
        self.arrow_rect.x = self.arrow_x
        self.arrow_rect.y = self.arrow_y
    def Hearth(self):
        self.hearth_imagem = self.Sprites[4]
        self.hearth_imagem = pygame.transform.scale(self.hearth_imagem,(50, 50))
        self.hearth_x, self.hearth_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.hearth_rect = pygame.Rect(self.hearth_x, self.hearth_y, 50, 50)
        self.hearth_rect.x = self.hearth_x
        self.hearth_rect.y = self.hearth_y
    def Enemy(self,enemy_value):
        self.enemy_power = enemy_value
        if self.enemy_power < 70:
            self.enemy_imagem = self.Sprites[5]
        elif self.enemy_power >= 70 and self.enemy_power < 90:
            self.enemy_imagem = self.Sprites[6]
        elif self.enemy_power >= 90:
            self.enemy_imagem = self.Sprites[7]
        self.enemy_imagem = pygame.transform.scale(self.enemy_imagem,(100, 80))
        self.enemy_x , self.enemy_y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
        self.enemy_rect = pygame.Rect(self.enemy_x, self.enemy_y, 100, 80)
        self.enemy_rect.x = self.enemy_x
        self.enemy_rect.y = self.enemy_y

def main():
    HEARTHS = 3
    RUPEES_COLECTED = 0 
    ARROWS_COLECTED = 0
    ENEMY_COLECTED = 0
    TIMER = 1800
    PAUSE = 100
    rupee_color = 0
    enemy_power = 0
    music_colid = pygame.mixer.Sound(os.path.join('sprits', 'getCandy.ogg'))
    music_enemy = pygame.mixer.Sound(os.path.join('sprits', 'hitMonster.wav'))
    font = pygame.font.Font(os.path.join('sprits', 'Roboto-Black.ttf'), 30)
    clock = pygame.time.Clock()
    player = Player()
    itens = Item()
    itens.Rupee(rupee_color)
    itens.Arrow()
    itens.Hearth()
    itens.Enemy(enemy_power)
    running = True
    while running == True:
        
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
        WINDOW.blit(itens.enemy_imagem,(itens.enemy_rect.x,itens.enemy_rect.y))
        if player.Rect.colliderect(itens.rupee_rect):
            if itens.rupee_color < 70:
                RUPEES_COLECTED += 1
                itens.rupee_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
                music_colid.play()
            elif itens.rupee_color >= 70 and itens.rupee_color < 90:
                RUPEES_COLECTED += 5
                itens.rupee_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
                music_colid.play()
            elif itens.rupee_color >= 90:
                RUPEES_COLECTED += 10
                itens.rupee_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                rupee_color = random.randint(0, 100)
                itens.Rupee(rupee_color)
                music_colid.play()
        if player.Rect.colliderect(itens.arrow_rect):    
            ARROWS_COLECTED += 1 
            itens.arrow_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
            itens.Arrow()
        if player.Rect.colliderect(itens.hearth_rect):    
            HEARTHS += 1
            itens.hearth_rect = pygame.Rect(random.randint(300,WIDTH - 300), random.randint(300,HEIGHT - 300),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
            itens.Hearth()
            music_colid.play()
            
        if player.Rect.colliderect(itens.enemy_rect):
            if itens.enemy_power < 70:
                ENEMY_COLECTED -= 1
                itens.enemy_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                enemy_power = random.randint(0, 100)
                itens.Enemy(enemy_power)
                music_enemy.play()
            elif itens.enemy_power >= 70 and itens.enemy_power < 90:
                ENEMY_COLECTED -= 2
                itens.enemy_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                enemy_power = random.randint(0, 100)
                itens.Enemy(enemy_power)
                music_enemy.play()
            elif itens.enemy_power >= 90:
                ENEMY_COLECTED -= 3
                itens.enemy_rect = pygame.Rect(random.randint(300,(WIDTH - 300)), random.randint(300,(HEIGHT - 300)),SPRITES_WIDTH/2, SPRITES_HEIGHT/2)
                enemy_power = random.randint(0, 100)
                itens.Enemy(enemy_power)
                music_enemy.play()
            HEARTHS+=ENEMY_COLECTED
        
        if HEARTHS==0:
            points = font.render(f"TOTAL DE RUPPEES COLETADOS: {RUPEES_COLECTED} ",True, (255,255,255))
            points_rect = points.get_rect(center = (WIDTH/2, HEIGHT/2))
            WINDOW.blit(points,points_rect)
            PAUSE -= 1
            if PAUSE==0:
                running = False     
            
        
        score_text = font.render(f'Rupees: {RUPEES_COLECTED}', True, (255, 255, 255))
        WINDOW.blit(score_text, (900, 20))
        arrow_text = font.render(f'Arrows: {ARROWS_COLECTED}', True, (255, 255, 255))
        WINDOW.blit(arrow_text, (1100, 20))
        hearth_text = font.render(f'HP: {HEARTHS}', True, (255, 255, 255))
        WINDOW.blit(hearth_text, (1300,20))
        emeny_text = font.render(f'HP: {HEARTHS}', True, (255, 255, 255))
        WINDOW.blit(emeny_text, (1300,20))
        
        timer = font.render(f'Tempo: {TIMER/60:.1f}',True, (255,255,255))
        WINDOW.blit(timer, (30,20))
        
        TIMER -=1
        if TIMER<0:
            TIMER = 0
            if TIMER==0:
                points = font.render(f"TOTAL DE RUPPEES COLETADOS: {RUPEES_COLECTED} ",True, (255,255,255))
                points_rect = points.get_rect(center = (WIDTH/2, HEIGHT/2))
                WINDOW.blit(points,points_rect)
                
                PAUSE -=1
                if PAUSE==0:
                    running = False
        
        pygame.display.flip()
        clock.tick(FPS)
        
        
    pygame.quit()

if __name__ == "__main__":
    main()