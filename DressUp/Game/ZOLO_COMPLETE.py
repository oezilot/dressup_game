import pygame # funktionen aus der pygame-library aufrufen die wir benötigen
import random # funktion die random zahlen generieren kann
from pygame.locals import (
    RLEACCEL, # verbessert die images
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.mixer.init() # mixer für soundeffekts starten
pygame.init() # pygame starten, damit man es benutzen kann

# pygame-fenster definieren mit höhe, breite und caption
SCREEN_HEIGHT = 600 # höhe
SCREEN_WIDTH = 900 # breite
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # fenster definieren
pygame.display.set_caption("DressUp") 

clock = pygame.time.Clock() #???

# musik hochladen
moving_sound = pygame.mixer.Sound("Audio/jump.wav")
victory_sound = pygame.mixer.Sound("Audio/success.wav")
defeat_sound = pygame.mixer.Sound("Audio/game_over.mp3")
button_sound = pygame.mixer.Sound("Audio/button.mp3")
collision_sound = pygame.mixer.Sound("Audio/collision.mp3")

# bilder hochladen
BACKGROUND_IMAGE = pygame.image.load("backgrounds/hintergrund.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

button1_image = pygame.image.load("backgrounds/button_start.png") #bild hochladen
button2_image = pygame.image.load("backgrounds/button_retry.png")
titelbild_image = pygame.image.load("backgrounds/head_spiegel.png")
face2_image = pygame.image.load("backgrounds/face_mad.png")
star_image = pygame.image.load("backgrounds/star.png")

# player images (den Player in allen verschiedenen Outfitkombinationen) 
base_image = pygame.image.load("state/base.png")
# nur ober oder unterteil
shirt1_state = pygame.image.load("state/shirt1.png") 
shirt2_state = pygame.image.load("state/shirt2.png")
pant1_state = pygame.image.load("state/pant1.png")
pant2_state = pygame.image.load("state/pant2.png")
# ober und unterteil
shirt1_pant1_state = pygame.image.load("state/shirt1_pant1.png") #1von4
shirt1_pant2_state = pygame.image.load("state/shirt1_pant2.png") #2von4
shirt2_pant1_state = pygame.image.load("state/shirt2_pant1.png") #3von4
shirt2_pant2_state = pygame.image.load("state/shirt2_pant2.png") #gutesoutfit: 4von4

class Button: 
    def __init__(self, x, y, image, width, height):
        self.image = pygame.transform.scale(image, (width, height))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) #coordinates of the top left edge of the button-rectangle are later given when the sprite object is defined. this is just genrals information

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
button = Button(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.8, button1_image, 191, 77) 
button2 = Button(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.8, button2_image, 191, 77) # (position, png, masse)  

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("state/base.png").convert_alpha()
        self.rect = self.surf.get_rect()
    clothing_state = "naked"

    def update(self, pressed_keys): 
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            moving_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            moving_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            moving_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            moving_sound.play()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT  
   
    def dress_up(self, enemy): 
        if self.clothing_state == "naked":
            if enemy == "shirt1":
                self.clothing_state = "shirt1"
                self.surf = pygame.image.load("./state/shirt1.png").convert_alpha()
            elif enemy == "shirt2":
                self.clothing_state = "shirt2"
                self.surf = pygame.image.load("./state/shirt2.png").convert_alpha()
            elif enemy == "shirt2":
                self.clothing_state = "shirt2"
                self.surf = pygame.image.load("./state/shirt2.png").convert_alpha()
            elif enemy == "pant1":
                self.clothing_state = "pant1"
                self.surf = pygame.image.load("./state/pant1.png").convert_alpha()
            elif enemy == "pant2":
                self.clothing_state = "pant2"
                self.surf = pygame.image.load("./state/pant2.png").convert_alpha() 
            elif enemy == "star":
                self.kill()
        elif self.clothing_state == "shirt1":
            if enemy == "pant1": 
                self.clothing_state = "shirt1_pant1"
                self.surf = pygame.image.load("state/shirt1_pant1.png").convert_alpha()
            elif enemy == "pant2":
                self.clothing_state = "shirt1_pant2"
                self.surf = pygame.image.load("state/shirt1_pant2.png").convert_alpha() 
            elif enemy == "star": 
                player.reset()
            else:
                player.kill()
        elif self.clothing_state == "shirt2":
            if enemy == "pant1": 
                self.clothing_state = "shirt2_pant1"
                self.surf = pygame.image.load("state/shirt2_pant1.png").convert_alpha()
            elif enemy == "pant2":
                self.clothing_state = "shirt2_pant2"
                self.surf = pygame.image.load("state/shirt2_pant2.png").convert_alpha()
            elif enemy == "star": 
                player.reset()
            else:
                player.kill()
        elif self.clothing_state == "pant1":
            if enemy == "shirt1": 
                self.clothing_state = "shirt1_pant1"
                self.surf = pygame.image.load("state/shirt1_pant1.png").convert_alpha()
            elif enemy == "shirt2":
                self.clothing_state = "shirt2_pant1"
                self.surf = pygame.image.load("state/shirt2_pant1.png").convert_alpha() 
            elif enemy == "star": 
                player.reset()
            else:
                player.kill()
        elif self.clothing_state == "pant2":
            if enemy == "shirt1": 
                self.clothing_state = "shirt1_pant2"
                self.surf = pygame.image.load("state/shirt1_pant2.png").convert_alpha() 
            elif enemy == "shirt2":
                self.clothing_state = "shirt2_pant2"
                self.surf = pygame.image.load("state/shirt2_pant2.png").convert_alpha()
            elif enemy == "star": 
                player.reset()
            else:
                player.kill()
        else:
            if enemy == "star":
                player.reset()
            else:
                player.kill()

    def reset(self):
        self.surf = pygame.image.load("state/base.png").convert_alpha()
        self.clothing_state = "naked"
player = Player() 
player.rect.center = (0,SCREEN_HEIGHT/2) 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyType):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("EnemyImages/"+enemyType+".png").convert_alpha()
        self.rect = self.surf.get_rect( # rectangle represents the dimensions of the image
            center = (SCREEN_WIDTH + 20, random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(5, 7)
        self.enemyType = enemyType

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
mirror = Enemy("mirror2")
mirror.rect = mirror.surf.get_rect(
    bottomright = (SCREEN_WIDTH,SCREEN_HEIGHT)
        )
mirror.speed = 0

ADDENEMY = pygame.USEREVENT + 1 #custom event, ???
ADDSPIEGEL = pygame.USEREVENT + 2 #+2 is there to be able to differentiate the first event from the other
pygame.time.set_timer(ADDENEMY, 1050)

enemies = pygame.sprite.Group() # eine Gruppe aus allen objekten(die mit dem bauplan der classes gebildet werden) machen 
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemies.add(mirror)
all_sprites.add(mirror)

running = True
gameMode = "startscreen"

while running:  
    event = pygame.event.poll()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    if event.type == QUIT:
        running = False
    
    if gameMode == "startscreen":
        screen.blit(BACKGROUND_IMAGE,(0,0))
        screen.blit(titelbild_image, (305, 20)) 
        button.draw(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.is_clicked(mouse_pos):
                button_sound.play()
                print("DressUp!")
                gameMode = "playing"
                player.rect.center = (0,SCREEN_HEIGHT/2)
                pygame.mixer.music.unload()
                pygame.mixer.music.load("Audio/hintergrund.mp3")
                pygame.mixer.music.play()

    if gameMode == "playing":
        screen.blit(BACKGROUND_IMAGE,(0,0))
        
        if event.type == ADDENEMY:
            choice = random.choice(
                [ "shirt1",
                  "shirt2",
                  "pant1",
                  "pant2",
                  "star"
                  ]
                )
            new_enemy = Enemy(choice)
            enemies.add(new_enemy) 
            all_sprites.add(new_enemy)

        colliding = pygame.sprite.spritecollide(player, enemies, True) 
        if colliding != []: 
            enemy = colliding[0] 
            if enemy.enemyType == "mirror2":
                gameMode = "exitscreen_spiegel"
                enemies.add(mirror)
                all_sprites.add(mirror)
                pygame.mixer.music.stop()
                victory_sound.play()
            else:
                player.dress_up(enemy.enemyType)
            collision_sound.play()
        
        pressed_keys = pygame.key.get_pressed() 
        player.update(pressed_keys) 
        enemies.update() 

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect) #???
        screen.blit(player.surf, player.rect)

        if not player.alive(): 
            gameMode = "exitscreen"
            pygame.mixer.music.stop()
            defeat_sound.play()
            
    elif gameMode == "exitscreen":
        screen.blit(BACKGROUND_IMAGE,(0,0))
        button2.draw(screen)
        screen.blit(face2_image, (SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2-66))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.is_clicked(mouse_pos):
                player.add(all_sprites)
                player.reset()
                button_sound.play()
                print("RETRY!")
                gameMode = "playing"
                player.rect.center = (0,SCREEN_HEIGHT/2)
                pygame.mixer.music.unload()
                pygame.mixer.music.load("Audio/hintergrund.mp3")
                pygame.mixer.music.play()

    elif gameMode == "exitscreen_spiegel":
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        button2.draw(screen)

        # das image des kompletten outfits, hier wird mit if jeden fall gezeigt für jedes verschiedene outfit
        if player.clothing_state == "naked":
            screen.blit(base_image, (390, 140)) # 100, 100 ist die position des bildes
        elif player.clothing_state == "shirt1":
            screen.blit(shirt1_state, (390, 140))
        if player.clothing_state == "shirt2":
            screen.blit(shirt2_state, (390, 140))
        if player.clothing_state == "pant1":
            screen.blit(pant1_state, (390, 140))
        if player.clothing_state == "pant2":
            screen.blit(pant2_state, (390, 140))
        if player.clothing_state == "shirt1_pant1":
            screen.blit(shirt1_pant1_state, (390, 140))
        if player.clothing_state == "shirt1_pant2":
            screen.blit(shirt1_pant2_state, (390, 140))
        if player.clothing_state == "shirt2_pant1":
            screen.blit(shirt2_pant1_state, (390, 140))
        if player.clothing_state == "shirt2_pant2":
            screen.blit(shirt2_pant2_state, (390, 140))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.is_clicked(mouse_pos):
                player.add(all_sprites)
                player.reset()
                print("RETRY!")
                gameMode = "playing"
                player.rect.center = (0,SCREEN_HEIGHT/2)
                pygame.mixer.music.unload()
                pygame.mixer.music.load("Audio/hintergrund.mp3")
                pygame.mixer.music.play()

    clock.tick(30)
    pygame.display.flip()
pygame.mixer.quit()
pygame.quit