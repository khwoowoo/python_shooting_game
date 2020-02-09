###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Add_on(Object):
    def __init__(self, scene, player, number):
        super().__init__()
        self.imageSetUp(scene.loadImageFileDict['resource/player/add-on.png'], 128, 512, 5, 0)
        self.tag = 'Add_on'
        self.nowScene = scene
        self.playerAddress = player
        self.curSprite = 0
        #몆 번째 에드온인지
        self.number = number
        self.attTime = 0.0

    def move(self):
        if self.number == 0:
            self.rect.x = self.playerAddress.rect.x - 100
            self.rect.y = self.playerAddress.rect.y - 150
        elif self.number == 1:
            self.rect.x = self.playerAddress.rect.x + 100
            self.rect.y = self.playerAddress.rect.y - 150
        elif self.number == 2:
            self.rect.x = self.playerAddress.rect.x - 200
            self.rect.y = self.playerAddress.rect.y - 200
        elif self.number == 3:
            self.rect.x = self.playerAddress.rect.x + 200
            self.rect.y = self.playerAddress.rect.y - 200

    def animation(self):
        self.curSprite = self.playerAddress.curSpriteImageFile
        if self.curSprite < 0:
            self.curSprite = 0
        if self.curSprite > 4:
            self.curSprite = 4;

        rect = (self.spriteWidth * self.curSprite , 0,  #이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

        self.image.fill((0, 0, 0, 0))
        self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
        self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
        self.rect = self.image.get_rect()  # 이미지 rect가져오기

    def Att(self, deltatime):
        self.attTime += deltatime

        if self.attTime > 5.0:
            self.attTime = 0
            self.nowScene.spriteBulletGroup.add(
                Bullet('resource/bullet/player_bullet_2.png', 47, 47, self.rect.x + 47 * 0.5, self.rect.y, [0, -100],
                       'Bullet_Add_on', self.nowScene))

    # 업데이트
    def update(self, deltatime):
        self.animation()
        self.move()
        self.Att(deltatime)

