from pygame import * 
from random import *

window = display.set_mode((700, 500)) 
display.set_caption("spase shooter") 
background = transform.scale(image.load("galaxy.jpg"),(700,500)) 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= 635:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15,20,4)
        bullet.add(bullets)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Enemy(GameSprite):
  def update(self):
      self.rect.y += self.speed
      global lost
      if self.rect.y > 500:
            self.rect.x = randint(6,634)
            self.rect.y = 0
            lost = lost+1 
             
          
      

player = Player("rocket.png",10,390,60,65,5)

enemys = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(0,620),0,80,50,randint(1,1))
    enemys.add(enemy)

bullets = sprite.Group()

lost=0
score=0



font.init()
font1 = font.SysFont('Arial', 36)



text_gamevin = font1.render(
    "вы победили:",1,(0,255,0)
)

text_lose = font1.render(
    "вы проиграли:",1,(255,0,0)
)

text_shopmenu = font1.render(
    "магазин:",1,(255,255,255)
)

text_shop = font1.render(
    "улучшение 2x баллов-10",1,(255,255,255)
)


#mixer.music.load('space.ogg') 
#mixer.music.play() 
#firesound = mixer.Sound('fire.ogg')
finish=False            
game = True
shootupdate = False

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.fire()
                #firesound.play()
            if e.key == K_b and score >=10:
                score -=10
                shootupdate =True
                text_shop = font1.render("улучшение купленно",1,(255,255,255))
                
                
           
    
    if not finish:
            

        window.blit(background,(0,0))
        window.blit(text_shopmenu,(400,0))
        window.blit(text_shop,(400,30))
        tex_lose = font1.render("пропущенно:" + str(lost),1, (255,255,255))
        window.blit(tex_lose ,(10,40))
        if sprite.groupcollide(bullets, enemys, True, True):
            score += 1
            enemy = Enemy("ufo.png", randint(0,620),0,80,50,randint(1,2))
            enemys.add(enemy)
            if shootupdate == True:
                score +=2
            
            
        if lost >= 20 or sprite.spritecollide(player, enemys, False):
            window.blit(text_lose,(350,250))
            finish= True
        
        
            window.blit(text_lose,(350,250))
            finish= True
        if score>= 50:
            window.blit(text_gamevin,(350,250))
            finish= True

        text_vin = font1.render("сбито:" + str(score),1, (255,255,255))
       
        window.blit(text_vin, (10,20))

    
    
        player.update()
        player.reset()
        bullets.update()
        bullets.draw(window)
        enemys.update()
        enemys.draw(window)
        display.update()
    
    time.delay(8)