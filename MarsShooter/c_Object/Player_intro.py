###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Player_intro(Object):
    def __init__(self, scene):
        super().__init__()
        # press key를 만들기 위하여 사용
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.tag = 'Player_intro'
        # 스피드 값
        self.speed = 200
        #이미지 설정
        self.imageSetUp(scene.loadImageFileDict['resource/player/player.png'], 128, 512, 0, 0)
        self.rect.x = 960
        self.rect.y = 540
        # nowScene
        self.nowScene = scene
        #sound
        self.bulletSound = pygame.mixer.Sound("resource/laser.wav")
        self.bulletSound.set_volume(0.5)

    # key
    def key(self, event):
        if event.type in [pygame.KEYDOWN]:
            #move
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moveLeft = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moveRight = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moveUp = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moveDown = True


        elif event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moveLeft = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moveRight = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moveUp = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moveDown = False
            if event.key == pygame.K_SPACE:
                self.spacePress = False

    #무기
    def weapon(self):
        if self.eWeaponState == WeaponState.EPRESS_GUN:
            self.attackTime -= 0.012

            if self.spacePress == True and self.attackTime < 0:
                self.attackTime = 0.1
                self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57, self.rect.y - 100, [0, -100], 'Bullet', self.nowScene))
                self.bulletSound.play()

    # position, speed 설정
    def setUp(self, _posX, _posy, _speed, tag):
        self.rect.x = _posX
        self.rect.y = _posy
        self.speed = _speed
        self.tag = tag

    # 이동
    def move(self, deltatime):
        if self.moveLeft == True:
            self.rect.x -= self.speed * deltatime
        if self.moveRight == True:
            self.rect.x += self.speed * deltatime
        if self.moveUp == True:
            self.rect.y -= self.speed * deltatime
        if self.moveDown == True:
            self.rect.y += self.speed * deltatime

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINSIZEX:
            self.rect.x = WINSIZEX
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > WINSIZEY:
            self.rect.y = WINSIZEY

    def animation(self, deltatime, posX, posY):
        if self.moveLeft == True or self.moveRight == True:
            self.animationTime += deltatime

            if self.animationTime > 0.4:
                if self.curSpriteImageFile < 0:
                    self.curSpriteImageFile = 0
                if self.curSpriteImageFile > 4:
                    self.curSpriteImageFile = 4

                rect = (self.spriteWidth * self.curSpriteImageFile, 0,  # 이미지의 위치, 크기를 사용하여 처리
                        self.spriteWidth, self.spriteHeight)

                self.image.fill((0, 0, 0, 0))
                self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
                self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
                self.rect = self.image.get_rect()  # 이미지 rect가져오기
                self.rect.x = posX
                self.rect.y = posY

                if self.moveLeft == True:
                    self.curSpriteImageFile -= 1
                elif self.moveRight == True:
                    self.curSpriteImageFile += 1
                self.animationTime = 0
        else:
            self.curSpriteImageFile = 2
            rect = (self.spriteWidth * self.curSpriteImageFile, 0,  # 이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

            self.image.fill((0, 0, 0, 0))
            self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
            self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
            self.rect = self.image.get_rect()  # 이미지 rect가져오기
            self.rect.x = posX
            self.rect.y = posY

    # 업데이트
    def update(self, deltatime):
        self.move(deltatime)
        self.animation(deltatime, self.rect.x, self.rect.y)